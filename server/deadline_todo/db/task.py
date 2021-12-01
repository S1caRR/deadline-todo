from .db_config import engine, async_session
from .exceptions import TaskNotFound
from deadline_todo.models.task import Task, TaskModel, TaskListModel

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound


class TaskDatabaseService:
    def __init__(self):
        self.engine = engine
        self.async_session = async_session

    async def fetch_tasks_list(self, user_id: int) -> TaskListModel:
        """
        Fetch all user's task from DB
        """
        async with self.async_session() as session:
            result = await session.execute(
                select(Task)
                .filter_by(user_id=user_id)
            )
            await session.commit()

        tasks_list = []
        for task in result.scalars().all():
            task = TaskModel.from_orm(task)
            tasks_list.append(task)

        tasks_list = TaskListModel(tasks=tasks_list)

        return tasks_list

    async def fetch_task(self, user_id: int, task_id: int) -> TaskModel:
        """
        Fetch one user's task from DB
        """
        async with self.async_session() as session:
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

    async def add_new_task(self, task_data: TaskModel):
        """
        Create task in DB
        """
        async with self.async_session() as session:
            task_data = task_data.dict(exclude={'id', 'is_finished'})
            task = Task(**task_data)
            session.add(task)
            await session.commit()

    async def delete_task(self, user_id: int, task_id: int):
        """
        Delete task from DB
        """
        async with self.async_session() as session:
            task = await session.get(Task, task_id)
            if task and task.user_id == user_id:
                await session.delete(task)
                await session.commit()
            else:
                await session.close()
                raise TaskNotFound(task_id)

    async def update_task(self, user_id: int, task_id: int, new_task_data: TaskModel):
        """
        Update task in DB
        """
        async with self.async_session() as session:
            task = await session.get(Task, task_id)
            if task and task.user_id == user_id:
                task.name = new_task_data.name
                task.description = new_task_data.description
                task.deadline = new_task_data.deadline
                task.is_finished = new_task_data.is_finished

                await session.commit()
            else:
                await session.close()
                raise TaskNotFound(task_id)

