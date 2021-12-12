import deadline_todo.config as config
from deadline_todo.db.accounts import AuthDatabaseService
from deadline_todo.db.exceptions import UserNotFound

from aiohttp import web
import jwt


async def auth_middleware(app, handler):
    async def middleware(request):
        request.user = None
        jwt_token = request.headers.get('Authorization', None)
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, config.JWT_SECRET,
                                     algorithms=[config.JWT_ALGORITHM])
                request.user = await AuthDatabaseService.fetch_user_credentials(user_id=payload['user_id'])

            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                raise web.HTTPUnauthorized(text='Token is invalid')

            except UserNotFound as ex:
                raise web.HTTPUnauthorized(text=str(ex))

        return await handler(request)
    return middleware


def jwt_required(func):
    async def wrapper(request):
        if not request.user:
            raise web.HTTPUnauthorized(text='Authorization required!')
        return await func(request)
    return wrapper
