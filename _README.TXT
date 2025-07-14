# Aplicação Web - Sistema de Resumos de Processos Crime - Docker

Este repositório contém uma aplicação web desenvolvida em Flask para apoio ao tratamento de processos-crime com suporte a LLMs via Ollama. Toda a estrutura está encapsulada em Docker para facilitar a sua execução em qualquer máquina.

## Pré-requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Ollama](https://ollama.com/)

Por fim, dentro da pasta 03_Implementacao, terá de abrir o cmd e executar os seguintes comandos:
-docker build -t sistema-resumos-processos-crime .
-docker run -p 5000:5000 sistema-resumos-processos-crime