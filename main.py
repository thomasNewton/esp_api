from fastapi import FastAPI , Body , Request, Form, Depends, HTTPException, Response, Header
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from enum import Enum
from fastapi.encoders import jsonable_encoder
from models import *


def fake_hash_password(password: str):
    return "fakehashed" + password




app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/base", response_class=HTMLResponse )
def show_base_template( request : Request):
     return templates.TemplateResponse("base.html" , {"request" : request})

@app.get("/", response_class=HTMLResponse )
def show_main_template( request : Request):
     return templates.TemplateResponse("main.html" , {"request" : request})
 
@app.get("/login", response_class=HTMLResponse )
def show_login_template( request : Request):
     return templates.TemplateResponse("login.html" , {"request" : request})
 

@app.get("/create_user", response_class=HTMLResponse )
def show_create_user_template( request : Request):
     return templates.TemplateResponse("create_user.html" , {"request" : request})
 
 
@app.post("/create_user", response_model=User) # returns a User object to protect password
def read_new_user(request: Request , username: Annotated[str, Form()], password : Annotated[str , Form()], \
name : Annotated[str , Form()], email : Annotated[str , Form() ] | None = None  ):
    new_user ={"username" : username , "password" : password, "name": name , "email": email}
    pydantic_user = UserInDB( 
        name=name,
        username=username,
        disabled=False,
        email=email,
        hashed_password=fake_hash_password(password)  # temp
                         )
    return pydantic_user   # becase of the response model = user  .. no password returned 
 
 
@app.get("/esp_data", response_class=HTMLResponse )
def show_esp_data_template( request : Request):
     return templates.TemplateResponse("esp_view1.html" , {"request" : request})
 
@app.get("/chat", response_class=HTMLResponse )
def show_chat_template( request : Request):
     return templates.TemplateResponse("chat.html" , {"request" : request})



@app.post("/temp")
async def post_temperature(temp : Temperature ):
    temp_dict = dict(temp)
    print(temp)
    print(type(temp))
    print(type(temp_dict))
    print(temp_dict)
    return True   
    










"""

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









# this is just a route example not really meant to be be called no html was made to post to it
@app.post("/hero2/{id}") # example of param,query,body variables and embeding a query one into the body
def recieve_hero(id: int,ide: Annotated[int, Body(embed = True)], slurm : bool ,hero : Superhero):
    return hero
    
    
@app.post("/hero", response_model=Superhero) 
def recieve_hero(hero : Superhero):   
    jd = jsonable_encoder(hero)   
    # in python this is an object, fast api automatically converts it when its returned to the client.
    # but if we need it to be json for something else ( like a database)  we have to convert it explicitly
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