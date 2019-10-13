#!/bin/bash

# Use PORT environment variable if defined. Otherwise, default to 5555
PORT="${PORT:-5555}"

gunicorn -b 0.0.0.0:$PORT src.app:app
