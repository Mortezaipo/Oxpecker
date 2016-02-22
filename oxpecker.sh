#!/bin/sh
if [ "$#" -eq "0" ]; then
  echo "Run oxpecker command with arguments (install|check|start|stop|clean)"
  exit 0
fi

if [ "$1" = "install" ]; then
  echo "Oxpecker installing ...."
  python manage.py makemigrations
  python manage.py migrate
elif [ "$1" = "check" ]; then
  echo "Oxpecker checking ...."
elif [ "$1" = "start" ]; then
  echo "Oxpecker start services..."
  python manage.py runserver
elif [ "$1" = "stop" ]; then
  echo "Oxpecker stop services..."
elif [ "$1" = "clean" ]; then
  find . -iname "*pyc" -delete #FIXME
  find . -iname "[0-9]*.py*" -delete #FIXME
fi
