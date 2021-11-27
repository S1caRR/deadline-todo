from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from deadline_todo.db.db_config import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'User(id={self.id}, username={self.username}, password={self.password}, email={self.email})'