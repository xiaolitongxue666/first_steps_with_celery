from flask import Flask, request, jsonify
from celery.result import AsyncResult
from celery import Celery, Task

import tasks

app = Flask(__name__)

@app.route("/foo")
def foo():
    res = celery_app.send_task(name="foo")
    # print(res.get()) # Get task result will block request
    logger.info(f'/foo res.id : {res.id}')
    logger.info(f'/foo res.state : {res.state}')

    response = jsonify({'task_id': res.id, 'task_status': res.state, 'task_result': 'null'})
    response.status_code = 200
    return response

if __name__ == "__main__":

    celery_app = Celery('tasks', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')

    res = celery_app.send_task(name="foo")
    # print(res.get()) # Get task result will block request
    print(f'/foo res.id : {res.id}')
    print(f'/foo res.state : {res.state}')
