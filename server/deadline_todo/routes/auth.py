from deadline_todo.db.auth import *
import deadline_todo.config as config
from deadline_todo.db.exceptions import EmailAlreadyExist, UserNotFound

from aiohttp import web
from datetime import datetime, timedelta
from json import JSONDecodeError
import bcrypt
import jwt


auth_router = web.RouteTableDef()


@auth_router.post('/api/register')
async def register(request: web.Request):
    try:
        register_info = await request.json()

        username = register_info['username']
        email = register_info['email']
        password = bcrypt.hashpw(register_info['password'].encode(), bcrypt.gensalt()).decode()

        await add_new_user(username, email, password)

        return web.json_response({'message': 'User successfully registered!'},
                                 status=201)

    except EmailAlreadyExist as ex:
        return web.json_response({'message': str(ex)},
                                 status=400)

    except JSONDecodeError:
        return web.json_response({'message': 'Wrong input data'},
                                 status=400)


@auth_router.post("/api/login")
async def login(request: web.Request):
    try:
        login_info = await request.json()

        user = await fetch_user(email=login_info["email"])

        if not bcrypt.checkpw(login_info['password'].encode(), user.password.encode()):
            return web.json_response({'message': 'Wrong credentials'},
                                     status=401)

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
        return web.json_response({'message': str(ex)},
                                 status=404)

    except JSONDecodeError:
        return web.json_response({'message': 'Wrong input data'},
                                 status=400)
