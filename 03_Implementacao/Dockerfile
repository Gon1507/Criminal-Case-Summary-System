FROM python:3.13

WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copy the .Modelfile definitions
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

# Expose the application port
EXPOSE 5000

# Starts Ollama and the Flask app together
RUN chmod +x /app/start.sh
CMD ["./start.sh"]


