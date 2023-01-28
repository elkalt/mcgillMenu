#!/bin/bash

# script to update site quickly
cd /home/louismeunier/mysite/mcgillMenu/backend
git pull
# reqs
python3.8 -m pip install -r requirements.txt
# re-load
touch /var/www/louismeun
ier_pythonanywhere_com_wsgi.py