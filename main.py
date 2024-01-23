from fastapi import FastAPI
import logging
from celery import Celery
from config import CELERY_RESULT_BACKEND, CELERY_BROKER_URL
from task import scrape_and_save_data
app = FastAPI()

logging.basicConfig(level=logging.INFO)

celery = Celery(
    'task',
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

@app.get("/scrape")
async def start_scraping():
    logging.info('Scraping function invoked')
    task = scrape_and_save_data.delay()
    return {"message": "Web scraping initiated", "task_id": task}