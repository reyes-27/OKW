#!/bin/ash
echo"Apply db migrations"
python manage.py migrate
exec "#@"