from .db_init import engine, async_session
from deadline_todo.models.task import Task

from datetime import datetime
from sqlalchemy import select, insert, update, delete


async def fetch_tasks_list(user_id):
    """
    Fetch all user's task from DB by user_id
    :param user_id: user's id
    :return: list of tasks in dictionary format
    """
    async with async_session() as session:
        stmt = (
            select(Task).
            where(Task.user_id == user_id)
        )
        query_result = await session.execute(stmt)
        await session.commit()
    await engine.dispose()

    tasks = query_result.scalars().all()
    tasks_list = []
    for task in tasks:
        tasks_list.append({
            'task_id': task.id,
            'task_name': task.name,
            'task_desc': task.description,
            'deadline': task.deadline.isoformat()
        })

    return tasks_list


async def add_new_task(user_id, task_name=None, desc=None, deadline=None):
    async with async_session() as session:
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
    await engine.dispose()


async def delete_task(user_id: int, task_id: int):
    async with async_session() as session:
        stmt = (
            delete(Task).
            where(Task.id == task_id, Task.user_id == user_id).
            returning(Task)
        )
        deleted_task = await session.execute(stmt)
        await session.commit()
    await engine.dispose()

    if not deleted_task:
        raise Exception


async def update_task(user_id, task_id, new_task_name=None, new_desc=None, new_deadline=None):
    async with async_session() as session:
        stmt = (
            update(Task).
            where(Task.user_id == user_id, Task.id == task_id).
            values(
                name=new_task_name,
                description=new_desc,
                deadline=datetime.fromisoformat(new_deadline)
            ).
            returning(Task)
        )
        await session.execute(stmt)

        await session.commit()
    await engine.dispose()
