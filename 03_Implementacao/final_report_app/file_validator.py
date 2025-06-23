#Classe para fazer a validação de ficheiros 
#de acordo com a sua extensão.

class FileValidator:
    #Construtor com as extensões aceites.
    def __init__(self):
        self.extensoes_validas = ('.docx', '.doc', '.pdf')

    #Verificação da extensão.
    def is_valid(self, filename):
        return filename.lower().endswith(self.extensoes_validas)

