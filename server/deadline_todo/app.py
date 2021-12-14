from middlewares.auth_middleware import auth_middleware
from routes.accounts import auth_router
from routes.task import task_router
from db.accessor import Database
from sheduler.send_tasks import scheduler_run, scheduler_close
from extsystems.tg_bot import bot_start, bot_shutdown

from aiohttp import web
import aiohttp_cors


def init_app() -> web.Application:
    app = web.Application(middlewares=[auth_middleware])

    # Connect and disconnect DB accessor
    app.on_startup.append(Database.connect)
    app.on_cleanup.append(Database.disconnect)

    # Add telegram bot asyncio task
    app.on_startup.append(bot_start)
    app.on_cleanup.append(bot_shutdown)

    # Add scheduler asyncio task
    app.on_startup.append(scheduler_run)
    app.on_cleanup.append(scheduler_close)

    app.add_routes(auth_router)
    app.add_routes(task_router)

    cors = aiohttp_cors.setup(app, defaults={
        '*': aiohttp_cors.ResourceOptions(allow_credentials=True,
                                          expose_headers='*',
                                          allow_headers='*',
                                          allow_methods='*'
                                          )})
    for route in app.router.routes():
        cors.add(route)

    return app


if __name__ == '__main__':
    web.run_app(init_app(), host='localhost', port=8081)
