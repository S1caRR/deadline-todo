import deadline_todo.config as config
from deadline_todo.db.accounts import AuthDatabaseService
from deadline_todo.middlewares.auth_middleware import jwt_required
from deadline_todo.db.exceptions import LoginAlreadyExists, UserNotFound
from deadline_todo.models.pydantic_models import UserProfileModel, UserCredentialsModel

from aiohttp import web
from datetime import datetime, timedelta
from json import JSONDecodeError
from pydantic.error_wrappers import ValidationError
import bcrypt
import jwt
import logging


auth_router = web.RouteTableDef()


@auth_router.post('/api/register')
async def register(request: web.Request):
    """
    Register user method

    :param: request:
    :raise: web.HTTPBadRequest
    """
    try:
        data = await request.json()

        user_credentials = UserCredentialsModel(**data, exclude={'id'})
        user_credentials.password = bcrypt.hashpw(user_credentials.password.encode(), bcrypt.gensalt()).decode()

        await AuthDatabaseService().add_new_user(user_credentials)

        return web.json_response({'message': 'User successfully registered!'},
                                 status=201)

    except LoginAlreadyExists as ex:
        raise web.HTTPBadRequest(text=str(ex))

    except (JSONDecodeError, ValidationError):
        raise web.HTTPBadRequest(text='Wrong data format')


@auth_router.post('/api/login')
async def login(request: web.Request):
    """
    User's sign in by login and password

    Returns JWT Authorization token

    :param: request:
    :raise: web.HTTPUnauthorized
    :raise: web.HTTPBadRequest
    """
    try:
        data = await request.json()

        user_credentials = UserCredentialsModel(**data)

        user = await AuthDatabaseService.fetch_user_credentials(login=user_credentials.login)

        if not bcrypt.checkpw(user_credentials.password.encode(), user.password.encode()):
            raise web.HTTPUnauthorized(text='Wrong credentials')
        payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(seconds=config.JWT_EXP_DELTA_SECONDS)
        }
        jwt_token = jwt.encode(payload, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM)

        return web.json_response({
            'message': 'You are Successfully logged in!',
            'token': jwt_token
        },
            status=200)

    except UserNotFound as ex:
        logging.exception(ex)
        raise web.HTTPBadRequest(text=str(ex))

    except (JSONDecodeError, ValidationError) as ex:
        logging.exception(ex)
        raise web.HTTPBadRequest(text='Wrong data format')


@auth_router.get('/api/profile')
@jwt_required
async def get_profile(request: web.Request):
    """
    JWT Authorization token required!

    Get user profile data

    :param: request:
    :raise: web.HTTPBadRequest
    """
    try:
        user_id = request.user.id

        profile_data = await AuthDatabaseService.fetch_user_profile(user_id)

        return web.Response(body=profile_data.json(),
                            content_type='application/json',
                            status=200)

    except UserNotFound as ex:
        logging.exception(ex)
        raise web.HTTPBadRequest(text=str(ex))


@auth_router.patch('/api/profile')
@jwt_required
async def update_profile(request: web.Request):
    """
    JWT Authorization token required!

    Update user profile data

    :param: request:
    :raise: web.HTTPBadRequest
    """
    try:
        data = await request.json()
        user_id = request.user.id
        new_profile_info = UserProfileModel(**data)

        await AuthDatabaseService.update_profile(user_id, new_profile_info)

        return web.Response(text='Profile successfully updated',
                            status=200)

    except (JSONDecodeError, ValidationError) as ex:
        logging.exception(ex)
        raise web.HTTPBadRequest(text='Wrong data format')

    except UserNotFound as ex:
        logging.exception(ex)
        raise web.HTTPBadRequest(text=str(ex))


@auth_router.patch('/api/profile/reset_password')
@jwt_required
async def reset_password(request: web.Request):
    """
    JWT Authorization token required!

    Reset user's password

    :param: request:
    :raise: web.HTTPUnauthorized
    :raise: raise web.HTTPBadRequest
    """
    try:
        data = await request.json()
        user_id = request.user.id

        old_password = data.get('old_password', None)
        new_password = data.get('new_password', None)

        if old_password and new_password:

            if not bcrypt.checkpw(old_password.encode(), request.user.password.encode()):
                raise web.HTTPUnauthorized(text='Wrong password')

            hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()

            await AuthDatabaseService.reset_password(user_id, hashed_password)

        return web.Response(text='Password was successfully reset',
                            status=200)

    except JSONDecodeError as ex:
        logging.exception(ex)
        raise web.HTTPBadRequest(text='Wrong data format')

    except UserNotFound as ex:
        logging.exception(ex)
        raise web.HTTPBadRequest(text=str(ex))
