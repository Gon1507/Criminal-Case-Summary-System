import requests
import json
import docx2txt

def ler_arquivo_docx(caminho_arquivo):
    return docx2txt.process(caminho_arquivo)

url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}

caminho_do_arquivo = "uploads/Bacalhau.docx"  
conteudo_do_arquivo = ler_arquivo_docx(caminho_do_arquivo)

data = {
    "model": "Prototipo",
    "prompt": conteudo_do_arquivo,
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))
    
if response.status_code == 200:
    data = json.loads(response.text)
    resposta = data["response"]
    print(resposta)
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)