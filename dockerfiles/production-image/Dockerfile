FROM python:3.8.2-slim

COPY requirements*.txt /microservice/

RUN pip install -r /microservice/requirements.txt

COPY source /microservice/source
COPY config.yaml /microservice/

COPY model_bin/model.pkl /microservice/model_bin/model.pkl

WORKDIR /microservice

CMD ["uvicorn", "source.main:app", "--host=0.0.0.0", "--port=8000"]