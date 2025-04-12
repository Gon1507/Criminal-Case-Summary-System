from flask import Flask, render_template, request, redirect, url_for
import os
import docx2txt

app = Flask(__name__)

#pasta onde os ficheiros sao guardados
app.config['UPLOAD_FOLDER'] = 'uploads/'

#funcao auxiliar para determinar se o ficheiro
#é um documento docx
def docx_ou_nao(ficheiro):
    return ficheiro.endswith(".docx")

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

    texto_extraido = docx2txt.process(caminho)

    ficheiros_upload = []

    for ficheiro in os.listdir(app.config['UPLOAD_FOLDER']):
        if docx_ou_nao(ficheiro):
            ficheiros_upload.append(ficheiro)

    return render_template('index.html', files=ficheiros_upload, content=texto_extraido, filename=filename)

#se nao existir uma pasta upload cria uma e inicia a app
if __name__ == '__main__':
    if not os.path.exists('uploads/'):
        os.makedirs('uploads/')
    app.run(debug=True)