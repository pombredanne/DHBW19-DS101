FROM python:3.7.4

RUN pip install mlflow

RUN mkdir /mlflow/

CMD mlflow server \
    --backend-store-uri /mlflow \
    --default-artifact-root /mlflow \
    --host 0.0.0.0