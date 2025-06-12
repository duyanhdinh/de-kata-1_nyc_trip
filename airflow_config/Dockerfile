FROM apache/airflow:slim-2.11.0-python3.12

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

USER root
RUN apt-get update && apt-get install -y git

USER airflow