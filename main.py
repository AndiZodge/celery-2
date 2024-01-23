from fastapi import FastAPI
from task import scrape_and_save_data
from utils import get_logger

log = get_logger(logger_name="main", module="main")

app = FastAPI()

@app.get("/scrape")
async def start_scraping():
    log.info('Scraping function invoked')
    scrape_and_save_data.delay()
    return {"message": "Web scraping initiated"}