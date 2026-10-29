import re

#Com a ajuda da biblioteca re (regular expression)
#é possível a criação de um função que permita
#reformular o texto extraído dos ficheiros

class CleanText:
    def clean(self, text):
        #Conseguir remover tabs que possam existir depois da extração
        text = text.replace('\t', '')
        #Remover espaços iniciais ou finais desnecessários em cada linha
        text = '\n'.join([line.strip() for line in text.splitlines()])
        #Manter uma linha entre parágrafos
        text = re.sub(r'\n{3,}', '\n\n', text)
        #Remover espaços em branco no final de uma frase
        text = re.sub(r' +\n', '\n', text)

        return text
