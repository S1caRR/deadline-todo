from deadline_todo.db.auth import AuthDatabaseService
import deadline_todo.config as config
from deadline_todo.db.exceptions import EmailAlreadyExist, UserNotFound

from aiohttp import web
from datetime import datetime, timedelta
from json import JSONDecodeError
import bcrypt
import jwt


auth_router = web.RouteTableDef()
auth_db_service = AuthDatabaseService()


@auth_router.post('/api/register')
async def register(request: web.Request):
    """
    Register user method

    :param request:
    """
    try:
        data = await request.json()

        username = data.get('username')
        email = data.get('email')
        password = bcrypt.hashpw(data.get('password').encode(), bcrypt.gensalt()).decode()

        await auth_db_service.add_new_user(username, email, password)

        return web.json_response({'message': 'User successfully registered!'},
                                 status=201)

    except EmailAlreadyExist as ex:
        raise web.HTTPBadRequest(text=str(ex))

    except JSONDecodeError:
        raise web.HTTPBadRequest(text='Wrong input data')


@auth_router.post('/api/login')
async def login(request: web.Request):
    """
    Login user by email and password

    :param request:
    :return: json object with field 'token' which contains JWT Authorization token
    """
    try:
        data = await request.json()

        email = data.get('email')
        password = data.get('password')

        user = await auth_db_service.fetch_user(email=email)

        if user and password and not bcrypt.checkpw(password.encode(), user.get('password').encode()):
            return web.HTTPUnauthorized(text='Wrong credentials')
        payload = {
            'user_id': user.get('user_id'),
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
