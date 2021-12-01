from .db_config import engine, async_session
from .exceptions import LoginAlreadyExists, UserNotFound
from deadline_todo.models.user import User, UserModel

from sqlalchemy import select, or_
from sqlalchemy.exc import IntegrityError, NoResultFound


class AuthDatabaseService:
    def __init__(self):
        self.engine = engine
        self.async_session = async_session

    async def fetch_user(self, user_id=None, login=None) -> UserModel:
        """
        Fetch user from DB
        """
        async with self.async_session() as session:
            user = await session.execute(
                select(User).
                where(or_(User.login == login, User.id == user_id))
            )
            await session.commit()

        try:
            user = user.scalar_one()
            user = UserModel.from_orm(user)
            return user
        except NoResultFound as ex:
            raise UserNotFound(user_id=user_id, login=login) from ex

    async def add_new_user(self, user_credentials: UserModel):
        """
        Creates a new user in DB
        """
        async with self.async_session() as session:
            try:
                user_credentials = user_credentials.dict()
                user = User(**user_credentials)
                session.add(user)
                await session.commit()
            except IntegrityError as ex:
                await session.close()
                raise LoginAlreadyExists(user.login) from ex
