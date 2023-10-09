FROM python:3.8-slim

WORKDIR /app

ENV MONGO_SERVER="10.106.27.94"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py

CMD ["python", "app.py"]
