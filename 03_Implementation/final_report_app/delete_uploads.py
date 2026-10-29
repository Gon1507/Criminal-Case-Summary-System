import os

#Com a ajuda da biblioteca os (operating system)
#é possível ao reiniciar o servidor, que ficheiros
#que estariam dentro da pasta uploads, sejam removidos
#para uma melhor operabilidade da aplicação

class DeleteUploads:
    def limpar_uploads(self, pasta):
        #Verifica primeiro se a pasta existe
        if os.path.exists(pasta):
            #Percorre todos os ficheiros dessa pasta
            for filename in os.listdir(pasta):
                caminho = os.path.join(pasta, filename)
                #E se o caminho for um ficheiro apaga-o da pasta
                if os.path.isfile(caminho):
                    os.remove(caminho)