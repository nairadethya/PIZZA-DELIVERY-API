from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://postgres:Ade123@#/pizza_delivery',
    echo = True 
)

Base = declarative_video()

Session = sessionmaker()