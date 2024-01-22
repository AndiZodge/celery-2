import requests
from database import SessionLocal, NewsDB
from NewsBaseModel import NewsModel
from config import API_KEY

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
            print(ex)
        
    def start_scraping_process(self) -> None:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            scraped_data = response.json()
            if scraped_data.get('status') == 'ok':
                print('data scraped successfully')
                self.data = scraped_data.get('articles', [])
                # print(json.dumps(self.data))
    
        except Exception as ex:
            print(ex)

    def curate_scraped_data(self) -> None:
        try:
            parse_news_blog = [NewsModel(**news_blog) for news_blog in self.data]
            self.parse_data = parse_news_blog
            print('parsing completed')
        except Exception as ex:
            print(ex)

    def save_scraped_data(self) -> None:
        try:
            
            db = SessionLocal()
            i= 1
            for data in self.parse_data:
                print(i)
                i+=1
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
            print('all items added in DB')
            db.commit()
        except Exception as exx:
            print(exx)
        finally:
            db.close()
    

        

# ScrapingData()