#!/bin/bash
apt install -y python3-pip
apt install -y mysql-client
python3 -m pip install flask
python3 -m pip install json
python3 -m pip install pymysql
python3 -m pip install 
export FLASK_APP = ../flask/app.py
nohup python3 -m flask run -h 0.0.0.0 --port 80 >/dev/null 2>&1 &