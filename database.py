from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""The create_engine function is used to create a SQLAlchemy engine, 
which provides a source of connectivity to a particular database.

The declarative_base function is used to create a base class for declarative SQLAlchemy models. 
It serves as a base class for all ORM classes defined in the application.

The sessionmaker class is a factory for creating SQLAlchemy sessions. 
Sessions are used to interact with the database and perform database 
operations such as querying, inserting, updating, and deleting records.

"""

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

"""sqlite:/// indicates the database dialect or driver used, which in this case 
is SQLite. The three slashes (///) indicate that the URL is in the "file" format 
rather than a networked database../sql_app.db represents the path to the SQLite 
database file. The dot (.) indicates the current directory, and sql_app.db is 
the name of the SQLite database file.
"""
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
"""The first argument, SQLALCHEMY_DATABASE_URL, is the URL or connection string for the database. 
It specifies the database type and location.
The connect_args parameter is an optional argument that allows passing additional arguments
to the underlying database driver during the connection setup.
In this case, the connect_args dictionary contains a single key-value pair: 
"check_same_thread": False. This argument is specific to SQLite databases 
and is used to disable a check that ensures SQLite connections are only used
by the same thread that created them. Setting it to False allows multiple threads 
to use the connection.
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""sessionmaker function is used to create a session factory with specific configurations. 
autocommit=False indicates that SQLAlchemy should not automatically commit each individual 
database operation. 
bind=engine specifies the engine to be used by the session factory. 

"""

Base = declarative_base()