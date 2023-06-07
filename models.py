"""An ORM has tools to convert ("map") between objects in code and database tables ("relations").

With an ORM, you normally create a class that represents a table in a SQL database, each attribute of the class represents a column, with a name and a type.

For example a class Pet could represent a SQL table pets.

And each instance object of that class represents a row in the database."""

from pydantic import BaseModel, HttpUrl
from typing import List, Union





"""Pydantic's orm_mode will tell the Pydantic model to read the data even 
if it is not a dict, but an ORM model (or any other arbitrary object with attributes).
This way, instead of only trying to get the id value from a dict, as in:
id = data["id"]
it will also try to get it from an attribute, as in:
id = data.id
And with this, the Pydantic model is compatible with ORMs, 
and you can just declare it in the response_model argument in your path operations.
"""

class User(BaseModel):
    username: str
    email: str | None = None
    name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str

class Temperature(BaseModel):
    temperature : float   
    
    
    
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









"""




   
    class Size(BaseModel):
    rec_hz : int
    rec_vt : int
    min_hz : int | None
    min_vt : int | None
    max_hz : int | None
    max_vt : int | None

class Image(BaseModel):
    url : HttpUrl
    description : str | None
    image_name : str
    size : Size

class Superhero(BaseModel):
    name: str
    birth: int 
    death : int | None
    powers : set[str] | None
    allies : set | None
    image : Image | None
   

    
class Super_team(BaseModel):
    name : str
    founded : int
    members : list[Superhero]
    
    
    """