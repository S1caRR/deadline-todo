from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from pydantic import BaseModel, constr

from deadline_todo.db.db_config import Base


class User(Base):
    __tablename__ = "user"

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(50), nullable=False)
    password = Column('password', String(100), nullable=False)
    email = Column('email', String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'User(id={self.id}, username={self.username}, password={self.password}, email={self.email})'


class UserModel(BaseModel):
    id: int = None
    username: constr(max_length=50) = None
    password: constr(max_length=100)
    email: constr(max_length=50)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
