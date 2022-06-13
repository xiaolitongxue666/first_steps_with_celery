# tasks.py
from celery import Celery
from celery.exceptions import SoftTimeLimitExceeded

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost//')
app.conf.broker_url = 'redis://localhost:6379/0'

@app.task(name='add_with_hard_timeout', time_limit=10)
def add_with_hard_timeout(x, y):
    import time
    time.sleep(20)
    print('Normal process')
    return x + y


@app.task(name='add_with_soft_timeout', soft_time_limit=10)
def add_with_soft_timeout(x,y):
    try:
        import time
        time.sleep(20)
        print('Normal process')
        return x+y
    except SoftTimeLimitExceeded:
        print('Timeout process')
