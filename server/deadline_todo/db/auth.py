from .db_config import engine, async_session
from .exceptions import EmailAlreadyExist, UserNotFound
from deadline_todo.models.user import User

from sqlalchemy import select, insert, or_
from sqlalchemy.exc import IntegrityError


class AuthDatabaseService:
    def __init__(self):
        self.engine = engine
        self.async_session = async_session

    async def fetch_user(self, email=None, user_id=None):
        """
        Fetch SQLAlchemy models.User object from database by the email or user id
        :param email: user's email
        :param user_id: user's id
        :raise UserNotFound
        :return: SQLAlchemy models.User object
        """
        async with self.async_session() as session:
            stmt = (
                select(User).
                where(or_(User.email == email, User.id == user_id))
            )
            user = await session.execute(stmt)
            await session.commit()
        await self.engine.dispose()

        user = user.scalars().first()

        if user:
            return user
        else:
            raise UserNotFound(user_id=user_id, email=email)

    async def add_new_user(self, username, email, hashed_password):
        """
        Creates a new user in DB
        :param username: username
        :param email: email
        :param hashed_password: password
        :raise EmailAlreadyExist
        """
        async with self.async_session() as session:
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
                await session.commit()
            except IntegrityError as e:
                await session.close()
                raise EmailAlreadyExist(email) from e
            finally:
                await self.engine.dispose()
