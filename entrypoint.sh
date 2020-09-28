#!/bin/bash
set -e

case "$1" in
develop)
  echo "Running Development Server"
  #        echo -e "$EE_PRIVATE_KEY" | base64 -d > privatekey.json
  exec python main.py
  ;;
test)
  echo "Running tests"
  echo -e "$EE_PRIVATE_KEY" | base64 -d >privatekey.json
  exec pytest --cov=geodescriber geodescriber/tests/
  ;;
start)
  echo "Running Start"
  #        echo -e "$EE_PRIVATE_KEY" | base64 -d > privatekey.json
  if [ -f .venv/bin/activate ]; then
    echo "Load Python virtualenv from '.venv/bin/activate'"
    source .venv/bin/activate
  fi
  exec gunicorn -c gunicorn.py geodescriber:app
  ;;
*)
  exec "$@"
  ;;
esac
