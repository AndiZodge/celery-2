<!-- Run celery command -->
celery -A main.celery worker -l info 
celery -A main.celery worker -l info --loglevel=DEBUG
<!-- celery -A tasks.tasks worker -l info --loglevel=DEBUG -->

<!-- Run fastapi server -->
uvicorn main:app --reload