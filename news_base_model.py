from pydantic import BaseModel
from typing import Optional

class NewsModel(BaseModel):
    title: Optional[str]  = "No title present"
    description: Optional[str]  = "No description present"
    author: Optional[str]  = "No author present"
    publishedAt: Optional[str]  = "No publishedAt date present"
    content: Optional[str]  = "No content present"
    urlToImage: Optional[str]  = "No urlToImage present"
    url: Optional[str] = "No url present"
