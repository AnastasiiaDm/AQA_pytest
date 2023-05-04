FROM jenkins/jenkins:lts

USER root

#для того чтоб работать с терминала пайчарма
#WORKDIR /code
#COPY . .

RUN apt update
RUN apt-get install wget
RUN apt-get install unzip
RUN apt install chromium -y
RUN apt-get install -y libglib2.0 libnss3 libgconf-2-4 libfontconfig1 chromium-driver
RUN apt-get update && apt-get install -y chromium python3 pip git python3-venv
