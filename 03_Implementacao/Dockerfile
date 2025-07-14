FROM python:3.13

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN curl -fsSL https://ollama.com/install.sh | sh

COPY models/ /modelfiles/

RUN ollama serve & \
    sleep 10 && \
    ollama pull gemma3:4b && \
    ollama create capaModelo -f /modelfiles/capaModelo.Modelfile && \
    ollama create cotaModelo -f /modelfiles/cotaModelo.Modelfile && \
    ollama create inquiricaoModelo -f /modelfiles/inquiricaoModelo.Modelfile && \
    ollama create termoJuntadaModelo -f /modelfiles/termoJuntadaModelo.Modelfile && \
    ollama create notificacaoModelo -f /modelfiles/notificacaoModelo.Modelfile && \
    ollama create informacaoModelo -f /modelfiles/informacaoModelo.Modelfile && \
    ollama create ResumoCronologico -f /modelfiles/resumoCronologico.Modelfile

EXPOSE 5000

CMD sh -c "ollama serve & sleep 5 && python run.py"