# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from config import DATABSE_URL
# from sqlalchemy.orm import Session
# from typing import Annotated
# from fastapi import Depends



# engine = create_engine(DATABSE_URL)

# SessioLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_db():
#     db = SessioLocal()
#     try: 
#         yield db
#     finally:
#         db.close()

# db_dependency = Annotated[Session, Depends(get_db)]

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class NewsDB(Base):
    __tablename__ = 'news'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(length=1000))
    description = Column(String(length=10000, collation='utf8mb4_unicode_ci'))
    author = Column(String(length=1000))
    publishedAt = Column(String(length=100))
    content = Column(String(length=10000))
    urlToImage = Column(String(length=1000))
    url = Column(String(length=1000))

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
