from .db_init import engine, async_session
from deadline_todo.models.user import User

from sqlalchemy import select, insert, or_


async def fetch_user(email=None, user_id=None):
    """
    Fetch SQLAlchemy models.User object from database by the email or user id
    :param email: user's email
    :param user_id: user's id
    :return: SQLAlchemy models.User object
    """
    async with async_session() as session:
        stmt = (
            select(User).
            where(or_(User.email == email, User.id == user_id))
        )
        user = await session.execute(stmt)
        await session.commit()
    await engine.dispose()

    user = user.scalars().first()

    return user


async def add_new_user(username, email, hashed_password):
    async with async_session() as session:
        stmt = (
            insert(User).
            values(
                username=username,
                email=email,
                password=hashed_password
            )
        )
        try:
            await session.execute(stmt)
        except Exception:
            raise Exception
        await session.commit()
    await engine.dispose()