import requests
from .llm import LLM

#Classe que foi definida com a necessidade de se
#conseguir gerar um resumo geral de cada um dos ficheiros
#que será introduzido na aplicação

class CopLLM(LLM): 
    def process_file(self, content, modelo):

            #Dados a serem enviados no modelo
            payload = {
                "model": modelo,
                "prompt": content,
                "stream": False
            }

            #Envia-se o pedido POST ao Ollama e converte a resposta
            #em formato json
            response = requests.post(LLM.OLLAMA_URL, headers=LLM.OLLAMA_HEADERS, json=payload)
            try:
                resposta_json = response.json()
            except ValueError:
                raise ValueError(f"Resposta não é JSON: {response.text}")

            # MOSTRA A RESPOSTA NO TERMINAL (LOGS DO DOCKER)
            print("🛠️ DEBUG RESPONSE JSON:", resposta_json)

            if "error" in resposta_json:
                raise RuntimeError(f"Erro do Ollama: {resposta_json['error']}")

            if "response" not in resposta_json:
                raise KeyError(f"Campo 'response' não existe. Resposta completa: {resposta_json}")

            return resposta_json["response"]