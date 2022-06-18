# tasks.py
from celery import Celery
from celery.exceptions import SoftTimeLimitExceeded

import os
import subprocess

app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
#app.conf.broker_url = 'redis://localhost:6379/0'

@app.task(name='foo')
def foo():
    # os.system : just run subprocess with a command
    # os.system("/Users/liyong/Code/Python/Celery/first_steps_with_celery/rater.sh")

    # ls_process = subprocess.run(
    #     ["ls", "-l"],
    #     capture_output=True,
    #     encoding="utf-8"
    # )
    # print(ls_process)
    # print(ls_process.stdout)

    print("foo done")
    return "foo done"
    

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
