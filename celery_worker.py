# from celery import Celery
# from celery.schedules import crontab
# from config import CELERY_RESULT_BACKEND, CELERY_BROKER_URL

# celery = Celery(
#     'tasks',
#     broker=CELERY_BROKER_URL,
#     backend=CELERY_RESULT_BACKEND
# )

# celery.conf.beat_schedule = {
#     'scrape-every-minute': {
#         'task': 'main.scrape_and_save_data',
#         'schedule': crontab(minute='*/1'), 
#     },
# }

# celery.conf.timezone = 'UTC'

# # Import tasks
# celery.autodiscover_tasks(['main'])
