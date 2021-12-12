from deadline_todo.config import ENGINE

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


class Database:
    INSTANCE = None
    engine = None

    def __new__(cls, *args, **kwargs):
        if not cls.INSTANCE:
            cls.INSTANCE = super().__new__(cls, *args, **kwargs)
            cls.engine = create_async_engine(ENGINE)
        return cls.INSTANCE

    @classmethod
    async def close_connection(cls):
        if cls.engine:
            await cls.engine.dispose()

    @classmethod
    async def connect(cls, _):
        cls()

    @classmethod
    async def disconnect(cls, _):
        await cls().close_connection()

    def session(self):
        return Session(self.engine)


class Session:
    def __init__(self, engine):
        self.session = AsyncSession(engine, expire_on_commit=False)

    async def __aenter__(self):
        if self.session:
            return await self.session.__aenter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.__aexit__(exc_type, exc_val, exc_tb)
