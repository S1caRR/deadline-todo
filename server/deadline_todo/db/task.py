from .db_config import engine, async_session
from .exceptions import TaskNotFound
from deadline_todo.models.task import Task

from datetime import datetime
from sqlalchemy import select, insert, update, delete


class TaskDatabaseService:
    def __init__(self):
        self.engine = engine
        self.async_session = async_session

    async def fetch_tasks_list(self, user_id) -> list:
        """
        Fetch all user's task from DB

        :param user_id: user's id
        :return: list of tasks in dictionary format
        """
        async with self.async_session() as session:
            stmt = (
                select(Task).
                where(Task.user_id == user_id)
            )
            result = await session.execute(stmt)
            await session.commit()
        await self.engine.dispose()

        tasks = result.scalars().all()
        tasks_list = []
        for task in tasks:
            tasks_list.append(task.to_dict())

        return tasks_list

    async def fetch_task(self, user_id, task_id) -> dict:
        """
        Fetch one user's task from DB

        :param user_id: user's id
        :param task_id: task id
        :return: dict with task information
        """
        async with self.async_session() as session:
            stmt = (
                select(Task).
                where(Task.id == task_id, Task.user_id == user_id)
            )
            result = await session.execute(stmt)
            await session.commit()
        await self.engine.dispose()

        task = result.scalars().first()
        if not task:
            raise TaskNotFound(task_id)
        task = task.to_dict()

        return task

    async def add_new_task(self, user_id: int, task_name=None, desc=None, deadline=None):
        """
        Create task in DB

        :param user_id: user's id
        :param task_name: task name
        :param desc: task description
        :param deadline: task deadline
        """
        async with self.async_session() as session:
            stmt = (
                insert(Task).
                values(
                    name=task_name,
                    description=desc,
                    deadline=datetime.fromisoformat(deadline),
                    user_id=user_id
                )
            )
            await session.execute(stmt)

            await session.commit()
        await self.engine.dispose()

    async def delete_task(self, user_id: int, task_id: int):
        """
        Delete task from DB

        :param user_id: user's id
        :param task_id: task's id
        :raise TaskNotFound
        """
        async with self.async_session() as session:
            stmt = (
                delete(Task).
                where(Task.id == task_id, Task.user_id == user_id).
                returning(Task)
            )
            result = await session.execute(stmt)
            await session.commit()
        await self.engine.dispose()

        deleted_task = result.scalars().first()
        if not deleted_task:
            raise TaskNotFound(task_id)

    async def update_task(self, user_id, task_id,
                          task_name=None,
                          desc=None,
                          deadline=None,
                          is_finished=False):
        """
        Update task in DB

        :param user_id:
        :param task_id:
        :param task_name:
        :param desc:
        :param deadline:
        :param is_finished:
        :raise TaskNotFound
        :return:
        """
        async with self.async_session() as session:
            stmt = (
                update(Task).
                where(Task.user_id == user_id, Task.id == task_id).
                values(
                    name=task_name,
                    description=desc,
                    deadline=datetime.fromisoformat(deadline),
                    is_finished=is_finished
                ).
                returning(Task)
            )
            result = await session.execute(stmt)
            await session.commit()
        await self.engine.dispose()

        updated_task = result.scalars().first()
        if not updated_task:
            raise TaskNotFound(task_id)
