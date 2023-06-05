from pydantic import BaseModel, HttpUrl
from typing import List, Union
from fastapi.encoders import jsonable_encoder
import json
from schemas import *



def add_user(user: UserInDB, db:dict):
    db[user.username] = jsonable_encoder(user)
    with open("my_db.db", "w") as f:
        json.dump(db, f)
    return True

    
if __name__ == "__main__":
    user1 = User      # this doesnt create a user, it renames the User class to user1
    user1.name ="tom"
    user1.username = "sam"
    user1.disabled = False
    user1.email = "tom@tommy.com"
  
    
    user2 = UserInDB(
        username="sam",
        name="tom",
        email="tom@tommy.com",
        hashed_password="fake",
        disabled=False
        )

    
    json_user2 = jsonable_encoder(user2)   #  makes a dictonary froma pydantic model class
    jdumps_user2 = json.dumps(json_user2)  # makes a string from a dictonary
    #print(f"types user1: {type(user1)} user2: {type(user2)}  json_user2 {type(json_user2)}   jdumps_user2 {type(jdumps_user2)}")
    add_user(user2,fake_users_db)