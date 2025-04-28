import os
from final_report_app.file_validator import FileValidator
from final_report_app.doc_parser import DocParser

#Classe que vai gerir tudo o que tiver a ver com os ficheiros (validação, leitura, etc...).
class Manager:
    def __init__(self, upload_folder):
        #Definir a pasta onde os ficheiros que sao uploadados vão ficar
        #guardados, caso a pasta não exiat vai ser criada
        self.upload_folder = upload_folder
        os.makedirs(self.upload_folder, exist_ok=True)

        #Instancia o FileValidator() que vai validar as extensões dos ficheiros
        #e o DocParser que vai ler o conteúdo dos ficheiros.
        self.validator = FileValidator()
        self.parser = DocParser()

    #Método que vai retornar ficheiros válidos.
    def show_valid_files(self):
        #Percorre todos os ficheiros na pasta de upload e vai retornar
        #apenas aqueles que vão válidos, ou seja acabam com .docx, .doc ou .pdf
        ficheiros = os.listdir(self.upload_folder)
        validos = [f for f in ficheiros if self.validator.is_valid(f)]
        return validos

    #Método que vai ler o conteúdo dos ficheiros.
    def read_content(self, filename):
        #Pega no caminho do ficheiro dado como argumento e valida-o
        #utilizando o método is_valid() do FileValidator(), caso seja
        #válido ele vai converter o texto do documento para uma string
        #e vai retornar a mesma.
        caminho = os.path.join(self.upload_folder, filename)
        if self.validator.is_valid(filename):
            conteudo = self.parser.convert_file2content(caminho)
            return conteudo
        else:
            raise ValueError(f"Ficheiro {filename} inválido.")
