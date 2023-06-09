from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fake_users import make_fake_users

SQLALCHEMY_DATABASE_URL = "sqlite:///./my_esp.db"


def insert_user(user_pw: User_Pw):
    # Create an instance of UserInDB using the values from User_Pw
    user_in_db = UserInDB(
        username=user_pw.username,
        email=user_pw.email,
        name=user_pw.name,
        disabled=user_pw.disabled,
        hashed_pw=user_pw.hashed_password
    )
    
    # Establish a database session
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Session = sessionmaker(bind=engine)
    
    # Add the UserInDB instance to the session
    session = Session()
    session.add(user_in_db)
    
    try:
        # Commit the session to persist the changes
        session.commit()
    except:
        # Rollback the changes if an error occurs
        session.rollback()
        raise
    finally:
        # Close the session
        session.close()
        
users_list = make_fake_users(1)
print(users_list)

for x in users_list:
    insert_user(x)
    
    
    
f = open("myfile.txt", "w")

with open("file.txt", "w") as f:
    