from django.http import HttpResponse

from . import tasks


def home(request):
    tasks.write_file.delay()
    tasks.test_task.delay()
    return HttpResponse('<h1>Тест задачи celery</h1>')
