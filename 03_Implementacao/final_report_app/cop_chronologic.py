import requests
from .llm import LLM

#Classe que foi definida com a necessidade de se
#conseguir gerar um resumo cronológico com base 
#em vários resumos, estes gerados pelo agente Cop_LLM
#que gera respostas resumidas dos ficheiros inseridos

class CopChronologic(LLM):
    def process_file(self, exemplos, content):
        prompt = (
            "ATENÇÃO: O relatório final deve seguir EXATAMENTE a seguinte estrutura, e não deve conter qualquer conteúdo fora dessa estrutura:\n\n"
            "1. CRIME, 2. SUJEITOS PROCESSUAIS, 3. DESCRIÇÃO DOS FACTOS, 4. MODUS OPERANDI, 5. DILIGÊNCIAS DE INVESTIGAÇÃO, 6. CONCLUSÃO\n\n"
            "Usa apenas a informação presente nos resumos fornecidos. NÃO inventes ou acrescentes nada.\n\n"
        )

        prompt += "[EXEMPLOS DE RELATÓRIOS MODELO]\n"
        for ex_name, ex_text in exemplos.items():
            prompt += f"### {ex_name}\n{ex_text}\n\n"

        prompt += "[RESPOSTAS GERADAS]\n"
        for filename, resumo in content.items():
            prompt += f"### {filename}\n{resumo}\n\n"
            
        prompt += "\n\nAgora, gera apenas o Relatório Final, seguindo a estrutura exata abaixo, sem mais nada:\n\n"
        prompt += (
            "1. CRIME\n"
            "2. SUJEITOS PROCESSUAIS\n"
            "3. DESCRIÇÃO DOS FACTOS\n"
            "4. MODUS OPERANDI\n"
            "5. DILIGÊNCIAS DE INVESTIGAÇÃO\n"
            "6. CONCLUSÃO\n"
        )

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