from abc import ABC, abstractmethod

#A classe abstrata LLM serve como base para qualquer
#classe que queira efetuar uma comunicação com o servidor
#LLM (Ollama)

class LLM(ABC):
    #URL do servidor Ollama
    OLLAMA_URL = "http://host.docker.internal:11434/api/generate"
    #Cabeçalho HTTP
    OLLAMA_HEADERS = {"Content-Type": "application/json"}
    
    #Uma função a ser implementada nas subclasses, neste
    #caso às classes que funcionem como LLMs
    @abstractmethod
    def process_file(self, content):
        pass