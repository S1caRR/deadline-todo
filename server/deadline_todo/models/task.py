from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

from deadline_todo.db.db_config import Base


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    deadline = Column(DateTime, nullable=False)
    is_finished = Column(Boolean, nullable=False, default=False)
    user_id = Column(ForeignKey('user.id'), nullable=False)

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
