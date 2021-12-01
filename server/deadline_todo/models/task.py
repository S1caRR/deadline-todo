import datetime

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from pydantic import BaseModel, Field, constr

from deadline_todo.db.db_config import Base


class Task(Base):
    __tablename__ = "task"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50), nullable=False)
    description = Column('description', String(300), nullable=True)
    deadline = Column('deadline', DateTime, nullable=False)
    is_finished = Column('is_finished', Boolean, nullable=False, default=False)
    user_id = Column('user_id', ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            'task_id': self.id,
            'task_name': self.name,
            'task_description': self.description,
            'deadline': self.deadline.isoformat(),
            'is_finished': self.is_finished
        }

    def __repr__(self):
        return f'Task(id={self.id}, username={self.name}, password={self.deadline}, email={self.user_id})'


class TaskModel(BaseModel):
    id: int = None
    name: constr(max_length=50) = Field(alias='task_name')
    description: constr(max_length=300) = Field(None, alias='task_description')
    deadline: datetime.datetime
    is_finished: bool = None
    user_id: int = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
