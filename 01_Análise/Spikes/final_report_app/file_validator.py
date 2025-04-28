#Classe para fazer a validação de ficheiros de acordo com a sua extensão.
class FileValidator:

    def __init__(self):
        #Construtor com as extensões aceites.
        self.extensoes_validas = ('.docx', '.doc', '.pdf')

    def is_valid(self, filename):
        #Verificação da extensão.
        return filename.lower().endswith(self.extensoes_validas)

