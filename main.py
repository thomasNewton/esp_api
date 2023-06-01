from fastapi import FastAPI , Body , Request, Form, Depends, HTTPException
from models import *
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from enum import Enum
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_hash_password(password: str):
    return "fakehashed" + password

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user






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
    

@app.post("/temperature")
async def post_temperature(temp : Temperature ):
    temp_dict = dict(temp)
    print(temp)
    print(type(temp))
    print(type(temp_dict))
    print(temp_dict)
    return True






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