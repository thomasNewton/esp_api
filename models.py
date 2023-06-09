from pydantic import BaseModel
from sqlalchemy import Table, Column, String, Boolean, DateTime, Float
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
Base = declarative_base()

# db models
class UserInDB(Base):
    __tablename__ = "Users"
    username = Column(String, primary_key=True)
    email = Column(String)
    name = Column(String)
    disabled = Column(Boolean)
    hashed_pw =  Column(String)
"""   
class EspData(Base):
    __tablename__ = "Esp_Data"
    time_recieved =  Column(String, primary_key=True)
    c_temp = Column( Float )
    f_temp : Column( Float )
    humidity : Column( Float )
    c_heat_index : Column( Float )
    f_heat_index : Column( Float )

"""
# pydantic models - 
class User(BaseModel):
    username: str
    email: str | None = None
    name: str | None = None
    disabled: bool | None = None
    
class User_Pw(User):
    hashed_password: str

class Temperature(BaseModel):
    temperature : float   
    
class Esp_Data(BaseModel):
    c_temp : float
    f_temp : float
    humidity : float
    c_heat_index : float
    f_heat_index : float
    
class Esp_Data_Indb(Esp_Data):
    time_recieved : str










"""An ORM has tools to convert ("map") between objects in code and database tables ("relations").
With an ORM, you normally create a class that represents a table in a SQL database, each attribute of the class represents a column, with a name and a type.
For example a class Pet could represent a SQL table pets.
And each instance object of that class represents a row in the database.

Pydantic's orm_mode will tell the Pydantic model to read the data even 
if it is not a dict, but an ORM model (or any other arbitrary object with attributes).
This way, instead of only trying to get the id value from a dict, as in:
id = data["id"]
it will also try to get it from an attribute, as in:
id = data.id
And with this, the Pydantic model is compatible with ORMs, 
and you can just declare it in the response_model argument in your path operations.
"""
    
# for a demo on user authentication    
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}