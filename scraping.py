import requests
import logging

from database import SessionLocal, NewsDB
from NewsBaseModel import NewsModel
from config import API_KEY

logging.basicConfig(level=logging.INFO)

class ScrapingData:
    
    def __init__(self) -> None:
        self.data = None
        self.parse_data = None
        self.url  = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
        # self.start_process()
        
    def start_process(self):
        try:
            self.start_scraping_process()
            self.curate_scraped_data()
            self.save_scraped_data()
            
        except Exception as ex:
            logging.info(ex)
        
    def start_scraping_process(self) -> None:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            scraped_data = response.json()
            if scraped_data.get('status') == 'ok':
                logging.info('data scraped successfully')
                self.data = scraped_data.get('articles', [])
    
        except Exception as ex:
            logging.error(ex)

    def curate_scraped_data(self) -> None:
        try:
            parse_news_blog = [NewsModel(**news_blog) for news_blog in self.data]
            self.parse_data = parse_news_blog
            logging.info('parsing completed')
        except Exception as ex:
            logging.info(ex)

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
                
            logging.info('all items added in DB, now commiting all changes')
            db.commit()
        except Exception as exx:
            logging.error(exx)
        finally:
            db.close()
    

        
# if __name__ == '__main__':
# ScrapingData()