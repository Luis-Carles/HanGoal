FROM python:3

ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk/jre
RUN apt-get update && apt-get install -y g++ default-jdk
RUN pip install --upgrade pip
RUN pip install konlpy

COPY ./ ./app

CMD ["python","./app/main.py"]