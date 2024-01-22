from fastapi import FastAPI
# from celery import Celery
from tasks.tasks import complete_scraping, scrape_and_save_data
# from .tasks import scrape_and_save_data
# from tasks.tasks import scrape_and_save_data
from celery import Celery
from datetime import timedelta

from config import CELERY_RESULT_BACKEND, CELERY_BROKER_URL
from scraping import ScrapingData
app = FastAPI()


celery = Celery(
    'tasks',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

# Configure periodic task
# celery.conf.beat_schedule = {
#     'scrape-periodically': {
#         'task': 'tasks.scrape_and_save_data',
#         # 'schedule': timedelta(seconds=10), 
#     },
# }
# celery.autodiscover_tasks(['main'])

@celery.task
def scrape_and_save_data_v1():
    print('task invoked')
    obj = ScrapingData()
    obj.start_process()
    return True

@celery.task
def rev(a):
    return a[::-1]

@app.get("/scrape")
async def start_scraping():
    print('func invoked')
    # print(celery.send_task("tasks.tasks.complete_scraping"))
    task = rev.delay('aniket')
    print(task)
    return {"message": "Web scraping initiated", "task_id":1}