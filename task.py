from celery import Celery

from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
from scraping import ScrapingData
from celery.schedules import crontab

celery = Celery(
    'task',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

    
celery.conf.beat_schedule = {
    'run-every-minute': {
        'task': 'task.scrape_and_save_data',
        'schedule': crontab(),
    },
}

@celery.task
def scrape_and_save_data():
    obj = ScrapingData()
    obj.start_process()
    return {'message': 'scraping process completed'}
