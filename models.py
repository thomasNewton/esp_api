from pydantic import BaseModel, HttpUrl
from typing import List, Union


class Temperature(BaseModel):
    temperature : float 

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
    
# for a demo on user authentication    
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
