from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column('id', Integer, primary_key=True)
    login = Column('login', String(50), unique=True, nullable=False)
    password = Column('password', String(100), nullable=False)

    def __repr__(self):
        return f'User(id={self.id}, login={self.login}, password={self.password})'


class Task(Base):
    __tablename__ = "task"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50), nullable=False)
    description = Column('description', String(300), nullable=True)
    deadline = Column('deadline', DateTime, nullable=False)
    is_finished = Column('is_finished', Boolean, nullable=False, default=False)
    user_id = Column('user_id', ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'Task(id={self.id}, name={self.name}, description={self.description}, ' \
               f'deadline={self.deadline}, is_finished={self.is_finished}, user_id={self.user_id})'
