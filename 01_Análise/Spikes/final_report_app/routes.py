import os
import json
import requests
from flask import render_template, request, redirect, url_for, Blueprint, current_app
from cop_LLM.cop_llm import CopLLM

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

            cop_instance = CopLLM()
            for nome_ficheiro, conteudo in conteudos.items():
                respostas[nome_ficheiro] = cop_instance.process_file(conteudo)


    ficheiros = manager.show_valid_files()

    return render_template('index.html', files=ficheiros, respostas=respostas, conteudos=conteudos)

@bp.route('/favicon.ico')
def favicon():
    return '', 404