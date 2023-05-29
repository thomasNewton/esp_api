from pydantic import BaseModel, HttpUrl
from typing import List, Union

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
    