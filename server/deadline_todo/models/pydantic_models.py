from pydantic import BaseModel
from pydantic import Field, constr

from datetime import datetime
from typing import List


class UserModel(BaseModel):
    id: int = None
    login: constr(max_length=50)
    password: constr(max_length=100)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class TaskModel(BaseModel):
    id: int = None
    name: constr(max_length=50) = Field(alias='task_name')
    description: constr(max_length=300) = Field(None, alias='task_description')
    deadline: datetime
    is_finished: bool = None
    user_id: int = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class TaskListModel(BaseModel):
    tasks: List[TaskModel] = None
