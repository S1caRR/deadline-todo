import json

from deadline_todo.middlewares.auth_middleware import jwt_required
from deadline_todo.db.task import TaskDatabaseService
from deadline_todo.db.exceptions import TaskNotFound
from deadline_todo.models.pydantic_models import TaskModel

from aiohttp import web
from json import JSONDecodeError
from pydantic import ValidationError


task_router = web.RouteTableDef()
task_db_service = TaskDatabaseService()


@task_router.get('/api/tasks')
@jwt_required
async def api_tasks(request: web.Request) -> web.Response:
    """
    Method gets all user's tasks

    :param request:
    :return: json object with field 'data' witch contains list[dict[str, any]] of tasks
    """
    user_id = request.user.id
    is_finished = request.rel_url.query.get('is_finished', '')
    is_finished = True if (is_finished == 'true') else False

    tasks = await task_db_service.fetch_tasks_list(user_id, is_finished)

    return web.Response(body=tasks.json(exclude={'tasks': {'__all__': {'user_id'}}}, by_alias=True),
                        content_type='application/json',
                        status=200)


@task_router.get(r'/api/tasks/{task_id:\d+}')
@jwt_required
async def api_get_task(request: web.Request) -> web.Response:
    """
    Method gets task by id

    :param request:
    :return: json object with field 'data' witch contains task format dict[str, any]
    """
    try:
        user_id = request.user.id
        task_id = int(request.match_info.get('task_id'))

        task = await task_db_service.fetch_task(user_id, task_id)

        return web.Response(body=task.json(exclude={'user_id'}, by_alias=True),
                            content_type='application/json',
                            status=200)

    except TaskNotFound as ex:
        raise web.HTTPBadRequest(text=str(ex))


@task_router.post('/api/tasks')
@jwt_required
async def api_new_task(request: web.Request) -> web.Response:
    """
    Method creates task
    """
    try:
        data = await request.json()
        user_id = request.user.id

        task = TaskModel(user_id=user_id, **data)

        task_id = await task_db_service.add_new_task(task)

        return web.json_response({'id': task_id},
                                 status=201)

    except (JSONDecodeError, ValidationError):
        raise web.HTTPBadRequest(text='Wrong data format')


@task_router.delete(r'/api/tasks/{task_id:\d+}')
@jwt_required
async def api_delete_task(request: web.Request) -> web.Response:
    """
    Method deletes task by id
    """
    try:
        user_id = request.user.id
        task_id = int(request.match_info.get('task_id'))

        await task_db_service.delete_task(user_id, task_id)

        return web.json_response({'id': task_id},
                                 status=200)

    except TaskNotFound as ex:
        raise web.HTTPBadRequest(text=str(ex))


@task_router.patch(r'/api/tasks/{task_id:\d+}')
@jwt_required
async def api_update_task(request: web.Request) -> web.Response:
    """
    Method updates task by id
    """
    try:
        user_id = request.user.id
        task_id = int(request.match_info.get('task_id'))

        data = await request.json()
        task_data = TaskModel(**data)

        await task_db_service.update_task(user_id, task_id, task_data)

        return web.json_response({'id': task_id},
                                 status=200)

    except TaskNotFound as ex:
        raise web.HTTPBadRequest(text=str(ex))

    except (JSONDecodeError, ValidationError):
        raise web.HTTPBadRequest(text='Wrong data format')
