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
        respostas = {}
        erros = []

        for filename, conteudo in conteudos.items():
            nome_ficheiro = filename.lower()

            if "capa" in nome_ficheiro:
                modelo = "ModeloCapa"
            elif "cota" in nome_ficheiro:
                modelo = "ModeloCota"
            elif "inquirição" in nome_ficheiro:
                modelo = "ModeloInquiricao"
            elif "termo" in nome_ficheiro:
                modelo = "ModeloTermoJuntada"
            elif "notificação" in nome_ficheiro:
                modelo = "ModeloNotificacao"
            elif "informação" in nome_ficheiro:
                modelo = "ModeloInformacao"
            else:
                modelo = None

            print(f"[INFO] Modelo selecionado para {filename}: {modelo}")
            
            if modelo:
                resposta = self.cop_llm.process_file(conteudo, modelo)
                respostas[filename] = resposta
            else:
                erros.append(filename)
            
        #Devolvendo posteriormente o dicionario com as respostas geradas 
        return respostas
      
    #Método que permite gerir o Cop_Chronologic 
    def process_files_llm_chron(self, exemplos, respostas):
        #O mesmo irá receber os resumos individuais e vai
        #juntá-los todos num documento apenas, este de
        #forma cronológica
        return self.cop_chron.process_file(exemplos, respostas) 