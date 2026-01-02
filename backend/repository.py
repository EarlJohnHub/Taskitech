import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker

#Connection setup
db_url = "sqlite:///database.db"
engine = sa.create_engine(db_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# There is only one missing piece required specifically for FastAPI.

# In a web application, you don't want a single database connection that stays open forever. 
# You want a fresh connection for every user who visits your site, and you want that connection to close automatically when they are done.

# The Missing Piece: The get_db Dependency
# You need a function that "yields" a database session. In FastAPI, this is called a Dependency.