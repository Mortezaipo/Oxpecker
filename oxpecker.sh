#!/bin/sh
if [ "$#" -eq "0" ]; then
  echo "Run oxpecker command with arguments (install|check|start|stop|clean)"
  exit 0
fi

if [ "$1" = "install" ]; then
  echo "Oxpecker installing ...."
  python src/main.py install
elif [ "$1" = "check" ]; then
  echo "Oxpecker checking ...."
  python src/main.py check
elif [ "$1" = "start" ]; then
  echo "Oxpecker start services..."
  python main.py start
elif [ "$1" = "stop" ]; then
  echo "Oxpecker stop services..."
  python src/main.py stop
elif [ "$1" = "clean" ]; then
  find . -iname "*pyc" -delete #FIXME
fi