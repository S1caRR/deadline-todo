import deadline_todo.config as config
from deadline_todo.db.auth import fetch_user

from aiohttp import web
import jwt


async def auth_middleware(app, handler):
    async def middleware(request):
        request.user = None
        jwt_token = request.headers.get('authorization', None)
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, config.JWT_SECRET,
                                     algorithms=[config.JWT_ALGORITHM])
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return web.json_response({'message': 'Token is invalid'}, status=403)

            request.user = await fetch_user(user_id=payload['user_id'])
        return await handler(request)

    return middleware


def login_required(func):
    async def wrapper(request):
        if not request.user:
            return web.json_response({'message': 'Auth required'}, status=401)
        return func(request)

    return wrapper
