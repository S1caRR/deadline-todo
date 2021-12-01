from deadline_todo.db.auth import AuthDatabaseService
import deadline_todo.config as config
from deadline_todo.db.exceptions import LoginAlreadyExists, UserNotFound
from deadline_todo.models.user import UserModel

from aiohttp import web
from datetime import datetime, timedelta
from json import JSONDecodeError
from pydantic.error_wrappers import ValidationError
import bcrypt
import jwt


auth_router = web.RouteTableDef()
auth_db_service = AuthDatabaseService()


@auth_router.post('/api/register')
async def register(request: web.Request):
    """
    Register user method
    """
    try:
        data = await request.json()

        user_credentials = UserModel(**data, exclude={'id'})
        user_credentials.password = bcrypt.hashpw(user_credentials.password.encode(), bcrypt.gensalt()).decode()

        await auth_db_service.add_new_user(user_credentials)

        return web.json_response({'message': 'User successfully registered!'},
                                 status=201)

    except LoginAlreadyExists as ex:
        raise web.HTTPBadRequest(text=str(ex))

    except (JSONDecodeError, ValidationError):
        raise web.HTTPBadRequest(text='Wrong data format')


@auth_router.post('/api/login')
async def login(request: web.Request):
    """
    Login user by email and password

    :param request:
    :return: json object with field 'token' which contains JWT Authorization token
    """
    try:
        data = await request.json()

        user_credentials = UserModel(**data)

        user = await auth_db_service.fetch_user(login=user_credentials.login)

        if user and user_credentials.password and not bcrypt.checkpw(user_credentials.password.encode(),
                                                                     user.password.encode()):
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
        raise web.HTTPBadRequest(text=str(ex))

    except JSONDecodeError:
        raise web.HTTPBadRequest(text='Wrong input data')
