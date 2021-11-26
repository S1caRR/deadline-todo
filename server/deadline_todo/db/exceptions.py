class DBException(Exception):
    pass


class UserNotFound(DBException):
    def __init__(self, email=None, user_id=None):
        if user_id:
            super().__init__(
                f'User with id \'{user_id}\' not found'
            )
        elif email:
            super().__init__(
                f'User with email \'{email}\' not found'
            )


class EmailAlreadyExist(DBException):
    def __init__(self, email):
        super().__init__(
            f'User with email \'{email}\' already registered'
        )


class TaskNotFound(DBException):
    def __init__(self, task_id):
        super().__init__(
            f'Task with id \'{task_id}\' not found'
        )