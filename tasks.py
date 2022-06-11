# tasks.py
from celery import Celery

# Celery 第一个参数是当前module的名称，第二个参数是boker的关键字
# Redis you can use redis://localhost
#app = Celery('tasks', broker='pyamqp://guest@localhost//')
# or
app = Celery('tasks', backend='redis://localhost', broker='redis://localhost//')
app.conf.broker_url = 'redis://localhost:6379/0'


@app.task(time_limit=10)
def add(x, y):
    import time
    time.sleep(20)
    print('正常处理')

    return x + y

