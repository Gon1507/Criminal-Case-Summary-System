import requests
from .llm import LLM

#Classe que foi definida com a necessidade de se
#conseguir gerar um resumo geral de cada um dos ficheiros
#que será introduzido na aplicação

class CopLLM(LLM): 
    def process_file(self, content):

            #Dados a serem enviados no modelo
            payload = {
                "model": "ResumoGeral",
                "prompt": content,
                "stream": False
            }

            #Envia-se o pedido POST ao Ollama e converte a resposta
            #em formato json
            response = requests.post(LLM.OLLAMA_URL, headers=LLM.OLLAMA_HEADERS, json=payload)
            resposta_json = response.json()

            #Devolve apenas o campo da resposta
            return resposta_json["response"]