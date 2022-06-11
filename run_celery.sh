#!/bin/bash

set -x 

#celery -A tasks worker --loglevel=INFO --pool=solo --concurrency=1 # 日志级别INFO
celery -A tasks worker --loglevel=INFO --pool=prefork --concurrency=1 # 日志级别INFO
#celery -A tasks worker --loglevel=INFO --concurrency=1 # 日志级别INFO
#celery -A tasks worker --loglevel=INFO --pool=solo # 日志级别INFO
