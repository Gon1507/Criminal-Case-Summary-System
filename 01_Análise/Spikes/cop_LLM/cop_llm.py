import requests
from .llm import LLM

class CopLLM(): 
    def process_file(self, content):
            payload = {
                "model": "ResumoGeral",
                "prompt": content,
                "stream": False
            }

            response = requests.post(LLM.OLLAMA_URL, headers=LLM.OLLAMA_HEADERS, json=payload)
            resposta_json = response.json()

            return resposta_json["response"]