from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

import deadline_todo.config as config


engine = create_async_engine(
    config.ENGINE
)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)
