<!-- Run celery command -->
celery -A task.celery worker -l info -P solo
celery -A task.celery worker -l info --loglevel=INFO

<!-- Run beat for scheduler -->
celery -A task.celery beat --loglevel=info

<!-- Run fastapi server -->
uvicorn main:app --reload