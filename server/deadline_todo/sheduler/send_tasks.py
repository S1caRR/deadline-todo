from deadline_todo.extsystems.broadcast_tasks import broadcaster

import asyncio
import aioschedule


async def scheduler():
    try:
        aioschedule.every().day.at('7:00').do(broadcaster)
        while True:
            await aioschedule.run_pending()
            await asyncio.sleep(10)  # sacrificing precision for optimization
    except asyncio.CancelledError:
        pass


async def scheduler_run(app):
    app['scheduler'] = asyncio.create_task(scheduler())


async def scheduler_close(app):
    app['scheduler'].cancel()
    await app['scheduler']
