from fastapi import FastAPI , Body , Request, Form
from models import *
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from enum import Enum
from fastapi.encoders import jsonable_encoder


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def root_route():
    return {"root": "tis is it"}


@app.post("/hero", response_model=Superhero) 
def recieve_hero(hero : Superhero):   
    jd = jsonable_encoder(hero)   
    # in python this is an object, it is automatically converted by fastapi on return to json.
    # but if we need it to be json for something else ( like a database)  we have to convert it
    # it creates a dictonary ready for json.dumps()  not a single long string
    return hero


@app.post("/hero1")
def recieve_form_hero(request: Request , name: Annotated[str, Form()], age : Annotated[int , Form()] ):
    hero ={"name" : name , "birth" : age}
    msg ="This is the return message from submiting a Superhero with the form.\
        The form elements were loaded individually and a dictionary called hero was made in the route and sent back with the jinja template"
    return templates.TemplateResponse("form_hero.html" , {"request" : request , "hero" : hero, "msg" : msg})




@app.get("/form_hero" , response_class=HTMLResponse)
def form_hero( request : Request):
    hero =""
    msg = ""
    return templates.TemplateResponse("form_hero.html" , {"request" : request , "hero" : hero, "msg" : msg})
    



"""
# this is just a route example not really meant to be be called no html was made to post to it
@app.post("/hero2/{id}") # example of param,query,body variables and embeding a query one into the body
def recieve_hero(id: int,ide: Annotated[int, Body(embed = True)], slurm : bool ,hero : Superhero):
    return hero

class Tags(Enum):
    items = "items"
    users = "users"


@app.get("/items/", tags=[Tags.items])
async def get_items():
    return ["Portal gun", "Plumbus"]
    """