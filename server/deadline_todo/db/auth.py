from .db_config import engine, async_session
from .exceptions import EmailAlreadyExist, UserNotFound
from deadline_todo.models.user import User, UserModel

from sqlalchemy import select, insert, or_
from sqlalchemy.exc import IntegrityError


class AuthDatabaseService:
    def __init__(self):
        self.engine = engine
        self.async_session = async_session

    async def fetch_user(self, user_id=None, email=None) -> UserModel:
        """
        Fetch user from DB
        """
        async with self.async_session() as session:
            user = await session.execute(
                select(User).
                where(or_(User.email == email, User.id == user_id))
            )
            await session.commit()

        user = user.scalar_one()
        if user:
            user = UserModel.from_orm(user)
            return user
        else:
            raise UserNotFound(user_id=user_id, email=email)

    async def add_new_user(self, user_credentials: UserModel):
        """
        Creates a new user in DB
        """
        async with self.async_session() as session:
            try:
                task_data = user_credentials.dict()
                task = User(**task_data)
                session.add(task)
                await session.commit()
            except IntegrityError as ex:
                await session.close()
                raise EmailAlreadyExist(task.email) from ex
