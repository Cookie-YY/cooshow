#!/bin/sh
/root/anaconda3/bin/python3 env_test.py
/root/anaconda3/bin/python3 app.py
uwsgi --ini ../uwsgi.ini