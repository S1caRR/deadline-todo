from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

import deadline_todo.config as config


Base = declarative_base()


engine = create_async_engine(
    config.ENGINE
)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def make_db():
    """
    WARNING!!!
    It replaces all tables and deletes all data!
    """
    from deadline_todo.models.task import Task
    from deadline_todo.models.user import User

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
