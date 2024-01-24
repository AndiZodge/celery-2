from utils import get_celery
from config import API_KEY
from scraping import ScrapingData

celery = get_celery()


@celery.task
def scrape_and_save_data() -> str:
    """
        This is a celery task, which will start scraping process with a endpoint and then save scraped data in MySql
    """
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
        obj = ScrapingData(url)
        obj.start_process()
        return 'scraping process completed'
    
    except Exception as exc:
        return exc
