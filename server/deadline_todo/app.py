from middlewares.auth_middleware import auth_middleware
from routes.auth import auth_router
from routes.task import task_router
from aiohttp import web


async def init_app() -> web.Application:
    app = web.Application(middlewares=[auth_middleware])
    app.add_routes(auth_router)
    app.add_routes(task_router)
    return app


web.run_app(init_app())
