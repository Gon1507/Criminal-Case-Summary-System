#!/bin/sh
# Starts the Ollama server, waits until it is ready and then launches the Flask app.
set -e

ollama serve > /tmp/ollama.log 2>&1 &

for _ in $(seq 1 30); do
  curl -s http://localhost:11434/ > /dev/null && break
  sleep 1
done

exec python run.py
