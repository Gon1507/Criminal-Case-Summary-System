import requests
from .llm import *

class CopChronologic():
    def process_file(self, content):
        prompt = ""
        for filename, resumo in content.items():
            prompt += f"\n ### {filename}\n{resumo}"

        payload = {
            "model": "ResumoCronologico",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(LLM.OLLAMA_URL, headers=LLM.OLLAMA_HEADERS, json=payload)
        resposta_json = response.json()
        
        if "response" in resposta_json:
            return resposta_json["response"]
        elif "error" in resposta_json:
            return f"{resposta_json["error"]}"
        else:
            return "Erro"