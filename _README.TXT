# Aplicação Web - Sistema de Resumos de Processos Crime - Docker

Este repositório contém uma aplicação web desenvolvida em Flask para apoio ao tratamento de processos-crime com suporte a LLMs via Ollama. Toda a estrutura está encapsulada em Docker para facilitar a sua execução em qualquer máquina.

## Pré-requisitos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

Dentro da pasta 03_Implementacao, terá de abrir o CMD e executar os seguintes comandos:
docker build -t sistema-resumos-processos-crime .
docker run -p 5000:5000 sistema-resumos-processos-crime

Após a execução dos comandos Docker, abrir o terminal do container criado e executar o seguinte comando:
ollama serve

Na pasta 04_Teste, existem duas subpastas com ficheiros relativos a processos crime que podem ser yutilizados como exemplo para testar o sistema.

O ficheiro, denominado de "6. Relatขrio Final - Spoofing_331-24-4JGLSB", serve como base de um relatório final real escrito por um inspetor. Este pode ser utilizado ao enviar-se exemplos de relatórios finais reais para se poder usufruir da sua estrutura e linguagem para a geração de um relatório final.