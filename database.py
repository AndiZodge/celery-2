from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class NewsDB(Base):
    __tablename__ = 'news'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(length=1000, collation='utf8mb4_unicode_ci'))
    description = Column(Text(collation='utf8mb4_unicode_ci'))
    author = Column(String(length=1000, collation='utf8mb4_unicode_ci'))
    publishedAt = Column(String(length=100, collation='utf8mb4_unicode_ci'))
    content = Column(Text(collation='utf8mb4_unicode_ci'))
    urlToImage = Column(String(length=1000))
    url = Column(String(length=1000))

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
