#!/bin/bash

gunicorn -b :8000 main:app -t 300 --chdir /app --workers 4