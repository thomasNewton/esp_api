from pydantic import BaseModel
from sqlalchemy import  Column, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UserInDB(Base):
    __tablename__ = "Users"
    username = Column(String, primary_key=True)
    email = Column(String)
    name = Column(String)
    disabled = Column(Boolean)
    hashed_pw =  Column(String)
    
    
    
# pydantic models - 
class User(BaseModel):
    username: str
    email: str | None = None
    name: str | None = None
    disabled: bool | None = None
    
class User_Pw(User):
    hashed_password: str