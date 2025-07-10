import os
from final_report_app.file_validator import FileValidator
from final_report_app.doc_parser import DocParser
from final_report_app.clean_text import CleanText

#Classe que vai gerir tudo o que tiver a ver com os ficheiros (validação, leitura, etc...).
class Manager:
    def __init__(self, upload_folder, example_folder):
        #Definir a pasta onde os ficheiros que sao uploadados vão ficar
        #guardados, caso a pasta não exiat vai ser criada
        self.upload_folder = upload_folder
        self.example_folder = example_folder
        os.makedirs(self.upload_folder, exist_ok=True)
        os.makedirs(self.example_folder, exist_ok=True)

        #Instancia o FileValidator() que vai validar as extensões dos ficheiros
        #e o DocParser que vai ler o conteúdo dos ficheiros e o CleanText para
        #simplificar a forma que os documentos gerados se vêm
        self.validator = FileValidator()
        self.parser = DocParser()
        self.clean = CleanText()

    #Método que vai retornar ficheiros válidos.
    def show_valid_files(self, folder):
        #Percorre todos os ficheiros na pasta de upload e vai retornar
        #apenas aqueles que vão válidos, ou seja acabam com .docx, .doc ou .pdf
        ficheiros = os.listdir(folder)
        validos = [f for f in ficheiros if self.validator.is_valid(f)]
        return validos

    #Método que vai ler o conteúdo dos ficheiros.
    def read_content(self, filename, folder):
        #Pega no caminho do ficheiro dado como argumento e valida-o
        #utilizando o método is_valid() do FileValidator(), caso seja
        #válido ele vai converter o texto do documento para uma string
        #e vai retornar a mesma.
        caminho = os.path.join(folder, filename)
        if self.validator.is_valid(filename):
            conteudo = self.parser.convert_file2content(caminho)
            #O conteúdo vai ser então limpo para depois ser
            #bem apresentado a um inspetor
            conteudo = self.clean.clean(conteudo)
            return conteudo
        else:
            raise ValueError(f"Ficheiro {filename} inválido.")
        

