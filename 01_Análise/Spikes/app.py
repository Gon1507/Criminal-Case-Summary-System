import json
from flask import Flask, render_template, request, redirect, url_for
import os
import docx2txt
import requests

app = Flask(__name__)

#pasta onde os ficheiros sao guardados
app.config['UPLOAD_FOLDER'] = 'uploads/'
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_HEADERS = {"Content-Type": "application/json"}

#funcao auxiliar para determinar se o ficheiro
#é um documento docx
def docx_ou_nao(ficheiro):
    return ficheiro.endswith(".docx")

def ler_arquivo_docx(caminho_arquivo):
    return docx2txt.process(caminho_arquivo)

#no index a demonstração dos ficheiros (ou nao)
@app.route('/')
def index():
    ficheiros = []

    for ficheiro in os.listdir(app.config['UPLOAD_FOLDER']):
        if docx_ou_nao(ficheiro):
            ficheiros.append(ficheiro)

    return render_template('index.html', files=ficheiros, content=None)

#dar upload aos ficheiros
@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('files[]')

    for file in files:
        if file and docx_ou_nao(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
        
    return redirect(url_for('index'))

#abrir uma caixinha com o texto todo do ficheiro
#com a ajuda do metodo docx2text()
@app.route('/<filename>')
def ler_docx(filename):
    caminho = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    texto_extraido = ler_arquivo_docx(caminho)

    ficheiros_upload = []

    for ficheiro in os.listdir(app.config['UPLOAD_FOLDER']):
        if docx_ou_nao(ficheiro):
            ficheiros_upload.append(ficheiro)

    return render_template('index.html', files=ficheiros_upload, content=texto_extraido, filename=filename)

@app.route('/upload-rel-final/<filename>')
def apresentar_rel(filename):
    try:
        caminho = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        conteudo = ler_arquivo_docx(caminho)
        
        payload = {
            "model": "Prototipo",
            "prompt": conteudo,
            "stream": False
        }
        
        response = requests.post(OLLAMA_URL, headers=OLLAMA_HEADERS, json=payload)
        response.raise_for_status()
        
        resposta = json.loads(response.text)["response"]

        ficheiros = []

        for ficheiro in os.listdir(app.config['UPLOAD_FOLDER']):
            if docx_ou_nao(ficheiro):
                return render_template("index.html", files=ficheiros, content=resposta, filename=filename)
    
    except Exception as e:
        error_msg = f"Erro ao processar o arquivo: {str(e)}"
        ficheiros = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if docx_ou_nao(f)]
        return render_template("index.html", files=ficheiros, content=error_msg)

@app.route('/favicon.ico')
def favicon():
    return '', 404

#se nao existir uma pasta upload cria uma e inicia a app
if __name__ == '__main__':
    if not os.path.exists('uploads/'):
        os.makedirs('uploads/')
    app.run(debug=True)