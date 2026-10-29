# Web Application - Criminal Case Summary System - Docker

This repository contains a web application built with Flask to support the handling of criminal cases, with LLM support via Ollama. The whole structure is encapsulated in Docker so it can be run easily on any machine.

## Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

Inside the `03_Implementacao` folder, open a command prompt (CMD) and run the following commands:

docker build -t sistema-resumos-processos-crime .
docker run -p 5000:5000 sistema-resumos-processos-crime

Once the Docker commands have finished, open the terminal of the container you just created and run the following command:

ollama serve
