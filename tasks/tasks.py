from NewsBaseModel import NewsModel
from database import NewsDB, SessionLocal
from scraping import ScrapingData
# from ..celery import celery
from datetime import timedelta

from celery import Celery

celery = Celery('tasks', broker='pyamqp://guest@localhost//', backend='rpc://')


    
celery.conf.beat_schedule = {
    'scrape-periodically': {
        'task': 'tasks.scrape_and_save',
        'schedule': timedelta(seconds=10),  # Run every 10 seconds
    },
}
@celery.task
def scrape_and_save_data():
    print('task invoked')
    # obj = ScrapingData()
    # obj.start_process()
    return {'True': 'yes'}

    # ScrapingData()
celery.autodiscover_tasks(['main'])

@celery.task
def complete_scraping(a):
    import requests
    from config import API_KEY
    url  = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    response = requests.get(url)
    response.raise_for_status()
    scraped_data = response.json()
    if scraped_data.get('status') == 'ok':
        print('data scraped successfully')
        data = scraped_data.get('articles', [])
        parse_news_blog = [NewsModel(**news_blog) for news_blog in data]
        parse_data = parse_news_blog
        print('parsing completed')
        db = SessionLocal()
        i= 1
        for data in parse_data:
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
        db.close()
    return a[::-1]