from flask import Flask
from final_report_app.manager import Manager
import os

def create_app():

    #Inicialização da aplicação Flask na localização da pasta de templates.
    app = Flask(__name__, template_folder=os.path.join('..', 'interface', 'templates'))

    #Configuração da app criada.
    #Pasta onde os ficheiros vão ficar guardados.
    app.config['UPLOAD_FOLDER'] = 'uploads/'
    #Inicialização de um Manager com o caminho da pasta de uploads.
    app.config['MANAGER'] = Manager(upload_folder=app.config['UPLOAD_FOLDER'])

    #Importação e associação de um blueprint à aplicação.
    from .routes import bp
    app.register_blueprint(bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)



