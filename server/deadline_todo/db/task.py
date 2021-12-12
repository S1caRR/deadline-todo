from .engine import engine_maker
from .exceptions import TaskNotFound
from deadline_todo.models.schema import Task, User
from deadline_todo.models.pydantic_models import TaskModel, TaskListModel

from datetime import date, datetime

from sqlalchemy import select
from sqlalchemy.orm import Bundle
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession


class TaskDatabaseService:
    INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if not cls.INSTANCE:
            cls.INSTANCE = super().__new__(cls, *args, **kwargs)
        return cls.INSTANCE

    @staticmethod
    async def fetch_tasks_list(user_id: int, is_finished=None, by_date=None) -> TaskListModel:
        """
        Fetch all user's task from DB
        """
        async with engine_maker() as engine:
            async with AsyncSession(engine, expire_on_commit=False) as session:
                stmt = (
                    select(Task)
                    .where(Task.user_id == user_id)
                    .order_by(Task.deadline)
                )
                if is_finished:
                    stmt = stmt.where(Task.is_finished == is_finished)
                if by_date:
                    stmt = stmt.where(Task.deadline >= datetime.combine(by_date, datetime.min.time()),
                                      Task.deadline <= datetime.combine(by_date, datetime.max.time()))

                result = await session.execute(stmt)

        tasks_list = []
        for task in result.scalars().all():
            task = TaskModel.from_orm(task)
            tasks_list.append(task)

        tasks_list = TaskListModel(tasks=tasks_list)
        return tasks_list

    @staticmethod
    async def fetch_task(user_id: int, task_id: int) -> TaskModel:
        """
        Fetch one user's task from DB
        """
        async with engine_maker() as engine:
            async with AsyncSession(engine, expire_on_commit=False) as session:
                task = await session.execute(
                    select(Task).filter_by(user_id=user_id, id=task_id)
                )
                await session.commit()

        try:
            task = task.scalar_one()
            task = TaskModel.from_orm(task)
            return task
        except NoResultFound as ex:
            raise TaskNotFound(task_id) from ex

    @staticmethod
    async def add_new_task(task_data: TaskModel) -> int:
        """
        Create task in DB
        """
        async with engine_maker() as engine:
            async with AsyncSession(engine, expire_on_commit=False) as session:
                task_data = task_data.dict(exclude={'id', 'is_finished'})
                task = Task(**task_data)
                session.add(task)
                await session.commit()

            return task.id

    @staticmethod
    async def delete_task(user_id: int, task_id: int):
        """
        Delete task from DB
        """
        async with engine_maker() as engine:
            async with AsyncSession(engine, expire_on_commit=False) as session:
                task = await session.get(Task, task_id)
                if task and task.user_id == user_id:
                    await session.delete(task)
                    await session.commit()
                else:
                    await session.close()
                    raise TaskNotFound(task_id)

    @staticmethod
    async def update_task(user_id: int, task_id: int, new_task_data: TaskModel):
        """
        Update task in DB
        """
        async with engine_maker() as engine:
            async with AsyncSession(engine, expire_on_commit=False) as session:
                task = await session.get(Task, task_id)
                if task and task.user_id == user_id:
                    task.name = new_task_data.name
                    task.description = new_task_data.description
                    task.deadline = new_task_data.deadline
                    task.is_finished = new_task_data.is_finished

                    await session.commit()
                else:
                    raise TaskNotFound(task_id)

    @staticmethod
    async def tg_today_tasks() -> dict:
        async with engine_maker() as engine:
            async with AsyncSession(engine, expire_on_commit=False) as session:
                stmt = (
                    select(
                        Bundle('user', User.tg_id),
                        Bundle('task', Task.name, Task.description)
                    )
                    .join(Task.user_tasks)
                    .where(Task.deadline >= datetime.combine(date.today(), datetime.min.time()),
                           Task.deadline <= datetime.combine(date.today(), datetime.max.time()))
                    .where(User.tg_id is not None)
                    .where(Task.is_finished == False)
                )

                result = await session.execute(stmt)

        today_tasks = {}
        for row in result:
            tg_id = row.user.tg_id

            if not today_tasks.get(tg_id):
                today_tasks.update({tg_id: []})

            today_tasks[tg_id].append({
                    'task_name': row.task.name,
                    'task_desc': row.task.description
                })

        return today_tasks
