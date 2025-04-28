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

    #adicionada esta parte de codigo para se conseguir ler os ficheiros para por
    #automaticamente no site quando se faz upload
    conteudos = {}
    for file in ficheiros:
        conteudos[file] = manager.read_content(file)

    return render_template('index.html', files=ficheiros, respostas=respostas, conteudos=conteudos)

#Abrir uma caixinha com o texto todo do ficheiro.
#Com a ajuda do metodo show_valid_files() do Manager.
@bp.route('/<filename>')
def read_file(filename):
    manager = current_app.config['MANAGER']
    texto_extraido = manager.read_content(filename)
    ficheiros = manager.show_valid_files()
    return render_template('index.html', files=ficheiros, content=texto_extraido, filename=filename)

#Mandar o conteudo do ficheiro para o model do ollama para ser resumido.
@bp.route('/upload-rel-final/<filename>')
def show_summary(filename):
    manager = current_app.config['MANAGER']
    conteudo = manager.read_content(filename)

    payload = {
        "model": "Prototipo",
        "prompt": conteudo,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, headers=OLLAMA_HEADERS, json=payload)
    resposta = json.loads(response.text)["response"]

    ficheiros = manager.show_valid_files()
    return render_template('index.html', files=ficheiros, content=resposta, filename=filename)

@bp.route('/favicon.ico')
def favicon():
    return '', 404
