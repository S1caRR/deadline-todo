from deadline_todo.middlewares.auth_middleware import login_required
from deadline_todo.db.task import *

from aiohttp import web


task_router = web.RouteTableDef()


@login_required
@task_router.get("/api/tasks")
async def api_tasks(request: web.Request) -> web.Response:
    user_id = request.user.id
    tasks = await fetch_tasks_list(user_id)
    return web.json_response({
        "message": "success",
        "data": tasks
    }, status=200)


@login_required
@task_router.post("/api/tasks")
async def api_new_task(request: web.Request) -> web.Response:
    task = await request.json()

    user_id = request.user.id
    task_name = task["name"]
    task_desc = task["description"]
    deadline = task["deadline"]

    await add_new_task(user_id, task_name=task_name, desc=task_desc, deadline=deadline)

    return web.json_response({
        "message": "Task was successfully added!",
    },
        status=200)


@login_required
@task_router.delete("/api/tasks/{task_id}")
async def api_delete_task(request: web.Request) -> web.Response:
    user_id = request.user.id
    task_id = int(request.match_info["task_id"])

    await delete_task(user_id, task_id)

    return web.json_response({"status": "success", },
                             status=200)


@login_required
@task_router.patch("/api/tasks/{task_id}")
async def api_new_task(request: web.Request) -> web.Response:
    user_id = request.user.id
    task_id = request.match_info["task_id"]
    task = await request.json()

    await update_task(user_id, task_id,
                      new_task_name=task['name'],
                      new_desc=task['description'],
                      new_deadline=task['deadline'])
    return web.json_response({"message": "Task successfully updated!"},
                             status=200)
