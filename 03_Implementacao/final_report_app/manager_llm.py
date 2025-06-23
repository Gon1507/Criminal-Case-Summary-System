from .cop_llm import CopLLM
from .cop_chronologic import CopChronologic

class ManagerLLM:
    def __init__(self):
        #Criação das instâncias de cada um dos
        #tipos de LLMs presentes no projeto
        self.cop_llm = CopLLM()
        self.cop_chron = CopChronologic()
        
    #Método que permite gerir o Cop_LLM
    def process_files_llm(self, conteudos):
        #Onde irá receber um dicionario
        respostas = {}
        
        #E para cada ficheiro inserido, usa o modelo Cop_LLM
        #Para resumir e gerar cada uma das suas respostas individualmente
        for nome_ficheiro, conteudo in conteudos.items():
            respostas[nome_ficheiro] = self.cop_llm.process_file(conteudo)
        
        #Devolvendo posteriormente o dicionario com as respostas geradas 
        return respostas
      
    #Método que permite gerir o Cop_Chronologic 
    def process_files_llm_chron(self, respostas):
        #O mesmo irá receber os resumos individuais e vai
        #juntá-los todos num documento apenas, este de
        #forma cronológica
        return self.cop_chron.process_file(respostas) 
        
        