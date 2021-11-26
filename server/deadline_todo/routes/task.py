from deadline_todo.middlewares.auth_middleware import login_required
from deadline_todo.db.task import *
from deadline_todo.db.exceptions import TaskNotFound

from aiohttp import web
from json import JSONDecodeError


task_router = web.RouteTableDef()


@login_required
@task_router.get("/api/tasks")
async def api_tasks(request: web.Request) -> web.Response:
    user_id = request.user.id
    tasks = await fetch_tasks_list(user_id)
    return web.json_response({
        "message": "success",
        "data": tasks
    },
        status=200)


@login_required
@task_router.post("/api/tasks")
async def api_new_task(request: web.Request) -> web.Response:
    task = await request.json()

    user_id = request.user.id
    task_name = task.get('task_name')
    task_desc = task.get("task_description")
    deadline = task.get("deadline")

    await add_new_task(user_id, task_name=task_name, desc=task_desc, deadline=deadline)

    return web.json_response({"message": "Task was successfully added!"},
                             status=201)


@login_required
@task_router.delete(r'/api/tasks/{task_id}:\d+')
async def api_delete_task(request: web.Request) -> web.Response:
    try:
        user_id = request.user.id
        task_id = int(request.match_info["task_id"])

        await delete_task(user_id, task_id)

        return web.json_response({"status": "success", },
                                 status=200)

    except TaskNotFound as ex:
        return web.json_response({'message': str(ex)},
                                 status=404)

    except JSONDecodeError:
        return web.json_response({'message': 'Wrong input data'},
                                 status=400)


@login_required
@task_router.patch('/api/tasks/{task_id}')
async def api_new_task(request: web.Request) -> web.Response:
    try:
        user_id = request.user.id
        task_id = int(request.match_info.get('task_id'))

        data = await request.json()

        new_task_name = data.get('task_name')
        new_desc = data.get('task_description')
        new_deadline = data.get('deadline')
        is_finished = data.get('is_finished')

        await update_task(user_id, task_id,
                          task_name=new_task_name,
                          desc=new_desc,
                          deadline=new_deadline,
                          is_finished=is_finished)
        return web.json_response({'message': 'Task successfully updated!'},
                                 status=200)

    except TaskNotFound as ex:
        return web.json_response({'message': str(ex)},
                                 status=404)

    except JSONDecodeError:
        return web.json_response({'message': 'Wrong input data'},
                                 status=400)
