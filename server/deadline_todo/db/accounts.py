from .accessor import Database
from .exceptions import LoginAlreadyExists, UserNotFound
from deadline_todo.models.schema import User
from deadline_todo.models.pydantic_models import UserProfileModel, UserCredentialsModel

from sqlalchemy import select, or_
from sqlalchemy.exc import IntegrityError, NoResultFound


class AuthDatabaseService:
    INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if not cls.INSTANCE:
            cls.INSTANCE = super().__new__(cls, *args, **kwargs)
        return cls.INSTANCE

    @staticmethod
    async def fetch_user_credentials(user_id=None, login=None) -> UserCredentialsModel:
        """
        Fetch user credentials data from DB
        """
        async with Database().session() as session:
            user = await session.execute(
                select(User).
                where(or_(User.login == login, User.id == user_id))
            )
            await session.commit()

        try:
            user = user.scalar_one()
            user = UserCredentialsModel.from_orm(user)
            return user
        except NoResultFound as ex:
            raise UserNotFound(user_id=user_id, login=login) from ex

    @staticmethod
    async def fetch_user_profile(user_id: int) -> UserProfileModel:
        """
        Fetch user from DB
        """
        async with Database().session() as session:
            user = await session.execute(
                select(User).
                where(User.id == user_id)
            )
            await session.commit()

        try:
            user = user.scalar_one()
            user = UserProfileModel.from_orm(user)
            return user
        except NoResultFound as ex:
            raise UserNotFound(user_id=user_id) from ex

    @staticmethod
    async def add_new_user(user_credentials: UserCredentialsModel):
        """
        Creates a new user in DB
        """
        async with Database().session() as session:
            try:
                user_credentials = user_credentials.dict()
                user = User(**user_credentials)
                session.add(user)
                await session.commit()
            except IntegrityError as ex:
                await session.close()
                raise LoginAlreadyExists(user.login) from ex

    @staticmethod
    async def update_profile(user_id: int, profile_data: UserProfileModel):
        async with Database().session() as session:
            current_profile_data = await session.get(User, user_id)
            current_profile_data.tg_id = profile_data.tg_id
            await session.commit()

    @staticmethod
    async def reset_password(user_id: int, new_password: str):
        async with Database().session() as session:
            user_credentials = await session.get(User, user_id)
            user_credentials.password = new_password
            await session.commit()
