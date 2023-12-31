FROM python:3.10.13-bullseye

ENV AIRFLOW_HOME=/opt/airflow
ENV AIRFLOW__CORE__EXECUTOR=SequentialExecutor
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=sqlite:////opt/airflow/airflow.db
ENV AIRFLOW__WEBSERVER__SECRET_KEY=secret_key
ENV AIRFLOW__WEBSERVER__AUTHENTICATE=True
ENV AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.contrib.auth.backends.password_auth

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    freetds-bin \
    build-essential \
    libkrb5-dev \
    libsasl2-dev \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN pip install apache-airflow

USER root
RUN mkdir -p /opt/airflow && chmod 777 /opt/airflow && \
    mkdir -p /opt/airflow/dags && \
    mkdir -p /opt/airflow/logs && \
    mkdir -p /opt/airflow/plugins

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY *.py /opt/airflow/dags/
COPY airflow.sh airflow.sh


# Initialize the database
RUN airflow db init && \
    airflow users create \
    --username admin \
    --password admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@mail.com

EXPOSE 8080

CMD ["bash", "airflow.sh"]
