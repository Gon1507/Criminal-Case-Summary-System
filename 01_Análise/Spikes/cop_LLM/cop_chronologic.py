import requests
from .llm import *

class CopChronologic():
    def process_file(self, content):
        todas_respostas = [item.get("response", "") for item in content]
    
        texto_completo = "\n".join(todas_respostas)

        payload = {
            "model": "Prototipo",
            "prompt": texto_completo,
            "stream": False
        }

        response = requests.post(LLM.OLLAMA_URL, headers=LLM.OLLAMA_HEADERS, json=payload)
        resposta_json = response.json()

        return resposta_json["response"]