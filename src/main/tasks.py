from celery import shared_task
from proj.celery import app

from src.main.service import send


@app.task()
def write_file(email):
    send(email)
    return True


@app.task()
def test_task():
    print('Worked')
    return True
