from abc import ABC, abstractmethod

class LLM(ABC):
    OLLAMA_URL = "http://localhost:11434/api/generate"
    OLLAMA_HEADERS = {"Content-Type": "application/json"}
    
    @abstractmethod
    def process_file(self, content):
        pass