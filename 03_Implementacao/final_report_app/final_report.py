from flask import Flask
from final_report_app.manager import Manager
from final_report_app.manager_llm import ManagerLLM
from final_report_app.delete_uploads import DeleteUploads
import os

def create_app():
        
    limpar_uploads = DeleteUploads()

    #Inicialização da aplicação Flask na localização da pasta de templates.
    app = Flask(__name__, 
            template_folder=os.path.join('..', 'interface', 'templates'), 
            static_folder=os.path.join('..', 'interface', 'static'))

    #Configuração da app criada.
    #Pasta onde os ficheiros vão ficar guardados.
    app.config['UPLOAD_FOLDER'] = 'uploads/ficheiros'
    #Utilização da função limpar_uploads, para, ao reiniciar a aplicação
    #todos os ficheiros que existam anteriormente sejam removidos
    limpar_uploads.limpar_uploads(app.config['UPLOAD_FOLDER'])
    #Inicialização de um Manager com o caminho da pasta de uploads.
    app.config['MANAGER'] = Manager(upload_folder=app.config['UPLOAD_FOLDER'])
    app.config['LLM_MANAGER'] = ManagerLLM()

    #Importação e associação de um blueprint à aplicação.
    from .routes import bp
    app.register_blueprint(bp)

    return app


