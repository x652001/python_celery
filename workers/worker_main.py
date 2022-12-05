from celery import Celery
from workers.worker_add import Add

# Create Celery Instance
app = Celery('tasks',backend='redis://localhost:6379/', broker='redis://localhost:6379/')


@app.task
def add(x,y):
    return Add().add(x,y)

