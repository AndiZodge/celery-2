import requests
from requests.exceptions import Timeout

from database import SessionLocal, NewsDB
from news_base_model import NewsModel
from utils import get_logger

log = get_logger(logger_name="scraping_class", module="scraping_class")


class ScrapingData:
    
    def __init__(self, url: str) -> None:
        self.data = None
        self.parse_data = None
        self.url = url 
        
    def start_process(self) -> None:
        try:
            self.start_scraping_process()
            self.curate_scraped_data()
            self.save_scraped_data()
            
        except Exception as ex:
            log.error(ex)
        
    def start_scraping_process(self) -> None:
        try:
            with requests.get(self.url) as response:
                response.raise_for_status()
                scraped_data = response.json()
                log.info('data scraped successfully')
                self.data = scraped_data.get('articles', [])
                    
        except Timeout as tec:
            # We can add sleep of few seconds and can call api again if req
            log.error(tec)
            
        except Exception as ex:
            log.error(ex)

    def curate_scraped_data(self) -> None:
        try:
            parse_news_blog = [NewsModel(**news_blog) for news_blog in self.data]
            self.parse_data = parse_news_blog
            log.info('parsing completed')
        except Exception as ex:
            log.error(ex)

    def save_scraped_data(self) -> None:
        try:
            
            db = SessionLocal()
            for data in self.parse_data:
                news_article = NewsDB(
                    title=data.title,
                    description=data.description,
                    author=data.author,
                    publishedAt=data.publishedAt,
                    content=data.content,
                    urlToImage=data.urlToImage,
                    url=data.url
                )
                db.add(news_article)
                
            log.info('all items added in DB, now commiting all changes')
            db.commit()
        except Exception as exx:
            log.error(exx)
        finally:
            db.close()
    

        
# if __name__ == '__main__':
# ScrapingData()