import requests
from .llm import LLM

#Classe que foi definida com a necessidade de se
#conseguir gerar um resumo cronológico com base 
#em vários resumos, estes gerados pelo agente Cop_LLM
#que gera respostas resumidas dos ficheiros inseridos

class CopChronologic(LLM):
    def process_file(self, content):
        prompt = ""
        for filename, resumo in content.items():
            prompt += f"\n ### {filename}\n{resumo}"

        #Dados a serem enviados no modelo
        payload = {
            "model": "ResumoCronologico",
            "prompt": prompt,
            "stream": False
        }

        #Envia-se o pedido POST ao Ollama e converte a resposta
        #em formato json
        response = requests.post(LLM.OLLAMA_URL, headers=LLM.OLLAMA_HEADERS, json=payload)
        resposta_json = response.json()
        
        #Devolve apenas o campo da resposta
        return resposta_json["response"]