from deadline_todo.config import ENGINE

from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine


# Tip from SQLAlchemy docs https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html

# It’s advisable to invoke the AsyncEngine.dispose() method using await when using the AsyncEngine object in a scope
# that will go out of context and be garbage collected, as illustrated in the async_main function in the above example.
# This ensures that any connections held open by the connection pool will be properly disposed within an awaitable
# context. Unlike when using blocking IO, SQLAlchemy cannot properly dispose of these connections within methods
# like __del__ or weakref finalizers as there is no opportunity to invoke await. Failing to explicitly dispose of the
# engine when it falls out of scope may result in warnings emitted to standard out resembling the form
# RuntimeError: Event loop is closed within garbage collection.
@asynccontextmanager
async def engine_maker():
    engine = create_async_engine(
        ENGINE,
        echo=True
    )
    try:
        yield engine
    finally:
        await engine.dispose()
