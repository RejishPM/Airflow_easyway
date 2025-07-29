FROM apache/airflow:2.8.1

USER root
COPY requirements.txt /requirements.txt
RUN chown airflow: /requirements.txt

RUN mkdir -p /mlflow/artifacts && \
    chown -R airflow: /mlflow && \
    chmod -R 775 /mlflow

USER airflow
RUN pip install --no-cache-dir -r /requirements.txt
