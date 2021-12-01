class DBException(Exception):
    pass


class LoginAlreadyExists(DBException):
    def __init__(self, email):
        super().__init__(
            f'User with login \'{email}\' already exists'
        )


class UserNotFound(DBException):
    def __init__(self, login=None, user_id=None):
        if user_id:
            super().__init__(
                f'User with id \'{user_id}\' not found'
            )
        elif login:
            super().__init__(
                f'User with login \'{login}\' not found'
            )


class TaskNotFound(DBException):
    def __init__(self, task_id):
        super().__init__(
            f'Task with id \'{task_id}\' not found'
        )
