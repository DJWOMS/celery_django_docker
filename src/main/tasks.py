import requests
from celery import shared_task
from proj.celery import app

from src.main.service import send, save_categories


@app.task()
def write_file(email):
    send(email)
    return True


@app.task
def get_api():
    response = requests.get('https://api.publicapis.org/categories')
    if response.status_code == 200:
        save_categories(response.json())
        return True
    return False


@app.task()
def test_task():
    print('Worked')
    return True
