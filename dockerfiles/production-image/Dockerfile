FROM python:3.8.2-slim

COPY requirements.txt /microservice/requirements.txt

RUN pip install -r /microservice/requirements.txt
RUN pip install uvicorn==0.11.3

COPY utils /microservice/utils
COPY main.py /microservice/

COPY model_bin/model.pkl /microservice/model_bin/model.pkl

WORKDIR /microservice

Hello world!

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]