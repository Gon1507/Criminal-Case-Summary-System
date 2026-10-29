import requests
from .llm import LLM

#Classe que foi definida com a necessidade de se
#conseguir gerar um resumo cronológico com base 
#em vários resumos, estes gerados pelo agente Cop_LLM
#que gera respostas resumidas dos ficheiros inseridos

class CopChronologic(LLM):
    def process_file(self, exemplos, content):
        #Um inicio da prompt para tentar maximo que o relatorio gerado
        #siga a estrutura de um relatorio final real
        prompt = (
            "ATENÇÃO: O relatório final deve seguir EXATAMENTE a seguinte estrutura, e não deve conter qualquer conteúdo fora dessa estrutura:\n\n"
            "1. CRIME, 2. SUJEITOS PROCESSUAIS, 3. DESCRIÇÃO DOS FACTOS, 4. MODUS OPERANDI, 5. DILIGÊNCIAS DE INVESTIGAÇÃO, 6. CONCLUSÃO\n\n"
            "Usa apenas a informação presente nos resumos fornecidos. NÃO inventes ou acrescentes nada.\n\n"
        )

        #De seguida, todos os exemplos de relatorios finais reais (se existerem)
        #são adicionadas à prompt para seguir a sua estrutura e linguagem
        prompt += "[EXEMPLOS DE RELATÓRIOS MODELO]\n"
        for ex_name, ex_text in exemplos.items():
            prompt += f"### {ex_name}\n{ex_text}\n\n"

        #E, por fim, todas as respostas geradas de cada um dos ficheiros que foram inseridos
        #também serão acrescentadas à prompt
        prompt += "[RESPOSTAS GERADAS]\n"
        for filename, resumo in content.items():
            prompt += f"### {filename}\n{resumo}\n\n"
            
        #Para ter a certeza de que o relatorio gerado siga a estrutura de um real,
        #um reforço é introduzido
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
            "model": "ModeloResumoCronologico",
            "prompt": prompt,
            "stream": False
        }

        #Envia-se o pedido POST ao Ollama e converte a resposta
        #em formato json
        response = requests.post(LLM.OLLAMA_URL, headers=LLM.OLLAMA_HEADERS, json=payload)
        resposta_json = response.json()
        
        #Devolve apenas o campo da resposta
        return resposta_json["response"]