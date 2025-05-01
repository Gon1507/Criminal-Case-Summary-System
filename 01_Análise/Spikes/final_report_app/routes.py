import os
import json
import requests
from flask import render_template, request, redirect, url_for, Blueprint, current_app

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_HEADERS = {"Content-Type": "application/json"}

bp = Blueprint('main', __name__)

#No index a demonstração dos ficheiros (ou nao).
@bp.route('/')
def index():
    manager = current_app.config['MANAGER']
    ficheiros = manager.show_valid_files()
    return render_template('index.html', files=ficheiros, content=None)

#Dar upload aos ficheiros.
@bp.route('/upload', methods=['POST'])
def upload_file():
    manager = current_app.config['MANAGER']
    files = request.files.getlist('files[]')

    #Vai guardar todos os resumos de cada ficheiro
    respostas = {}
    conteudos = {}

    for file in files:
        if file and manager.validator.is_valid(file.filename):
            path = os.path.join(manager.upload_folder, file.filename)
            file.save(path)

            #Ler o conteúdo do ficheiro
            conteudo = manager.read_content(file.filename)
            conteudos[file.filename] = conteudo

            #Fazer as ceninhas do ollama
            payload = {
                "model": "Prototipo",
                "prompt": conteudo,
                "stream": False
            }

            response = requests.post(OLLAMA_URL, headers=OLLAMA_HEADERS, json=payload)
            resposta_json = response.json()

            #Ver se funcionou ou se deu erro
            if "response" in resposta_json:
                respostas[file.filename] = resposta_json["response"]
            else:
                respostas[file.filename] = f"Erro do modelo: {resposta_json.get('error', 'Erro desconhecido')}"

    ficheiros = manager.show_valid_files()

    return render_template('index.html', files=ficheiros, respostas=respostas, conteudos=conteudos)

@bp.route('/favicon.ico')
def favicon():
    return '', 404