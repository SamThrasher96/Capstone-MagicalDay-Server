#!/bin/bash

rm db.sqlite3
rm -rf ./magicaldayapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations magicaldayapi
python3 manage.py migrate magicaldayapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata guests
python3 manage.py loaddata locations
python3 manage.py loaddata staff
python3 manage.py loaddata staff_shifts
python3 manage.py loaddata ride_details
python3 manage.py loaddata show_details
python3 manage.py loaddata restaurant_details
python3 manage.py loaddata menu_items
python3 manage.py loaddata reservation