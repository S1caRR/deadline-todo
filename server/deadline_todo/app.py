from middlewares.auth_middleware import auth_middleware
from routes.auth import auth_router
from routes.task import task_router

from aiohttp import web
import aiohttp_cors


async def init_app() -> web.Application:
    app = web.Application(middlewares=[auth_middleware])
    app.add_routes(auth_router)
    app.add_routes(task_router)

    cors = aiohttp_cors.setup(app, defaults={
        '*': aiohttp_cors.ResourceOptions(allow_credentials=True,
                                          expose_headers='*',
                                          allow_headers='*',
                                          allow_methods='*')})
    for route in app.router.routes():
        cors.add(route)

    return app


web.run_app(init_app(), host='127.0.0.1', port=8081)
