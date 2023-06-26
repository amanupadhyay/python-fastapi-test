from database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    __tablename__ = 'users'
    
    username = Column(String, primary_key=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)


    