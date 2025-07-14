# Aplicação Web - Sistema de Resumos de Processos Crime - Docker

Este repositório contém uma aplicação web desenvolvida em Flask para apoio ao tratamento de processos-crime com suporte a LLMs via Ollama. Toda a estrutura está encapsulada em Docker para facilitar a sua execução em qualquer máquina.

## Pré-requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Ollama](https://ollama.com/)
- [Gemma](https://ollama.com/library/gemma3)

É necessário a instalação do modelo Gemma3:4b para se conseguir criar os agentes abaixo. Para isso utiliza-se o seguinte comando no CMD:
ollama pull gemma3:4b

É necessário também a criação de cada um dos agentes com os seguintes comandos no CMD:
- Os modelos encontram-se na pasta 03_Implementacao/models

ollama create ModeloCapa -f caminho-para_modelo_capa
ollama create ModeloCota -f caminho-para_modelo_cota
ollama create ModeloInquiricao -f caminho-para_modelo_inquiricao
ollama create ModeloTermoJuntada -f caminho-para_modelo_termo_juntada
ollama create ModeloNotificacao -f caminho-para_modelo_notificacao
ollama create ModeloInformacao -f caminho-para_modelo_informacao
ollama create ModeloResumoCronologico -f caminho-para_modelo_resumo_cronologico

Por fim, dentro da pasta 03_Implementacao, terá de abrir o CMD e executar os seguintes comandos:
docker build -t sistema-resumos-processos-crime .
docker run -p 5000:5000 sistema-resumos-processos-crime