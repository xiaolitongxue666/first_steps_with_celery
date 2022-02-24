#!/bin/bash

set -x 

celery -A tasks worker --loglevel=INFO # 日志级别INFO
