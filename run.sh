#!/bin/bash
cd /home/ubuntu/real-time-phishing-detection
python3 train_model.py
nohup gunicorn --bind 0.0.0.0:5000 app:app > app.log 2>&1 &