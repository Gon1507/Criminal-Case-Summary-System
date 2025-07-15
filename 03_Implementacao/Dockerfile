FROM python:3.13

WORKDIR /app
COPY . /app

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Instala o Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copia os ficheiros .Modelfile
COPY models/ /modelfiles/

RUN ollama serve & \
    sleep 5 && \
    ollama pull gemma3:4b && \
    ollama create ModeloCapa -f /modelfiles/capaModelo.Modelfile && \
    ollama create ModeloCota -f /modelfiles/cotaModelo.Modelfile && \
    ollama create ModeloInquiricao -f /modelfiles/inquiricaoModelo.Modelfile && \
    ollama create ModeloTermoJuntada -f /modelfiles/termoJuntadaModelo.Modelfile && \
    ollama create ModeloNotificacao -f /modelfiles/notificacaoModelo.Modelfile && \
    ollama create ModeloInformacao -f /modelfiles/informacaoModelo.Modelfile && \
    ollama create ModeloResumoCronologico -f /modelfiles/resumoCronologico.Modelfile

# Expõe a porta da aplicação
EXPOSE 5000

CMD ["python", "run.py"]


