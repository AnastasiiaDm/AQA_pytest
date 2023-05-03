#FROM jenkins/jenkins:lts
#
#USER root
#
#RUN apt-get update && apt-get install -y chromium python3 pip git python3-venv

#FROM jenkins/jenkins:lts
#
#USER root
#
##WORKDIR /code
##COPY . .
#
#RUN apt-get update && apt-get install -y chromium python3 pip git python3-venv \
#    && git clone https://github.com/AnastasiiaDm/AQA_pytest.git /code \
#    && cd /code \
#    && python3 -m venv venv \
#    && . venv/bin/activate \
#    && pip install -r requirements.txt \
#    && pytest seventeenth_hw/tests/ui_tests/test_main_page.py


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

#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_arm64.deb
#RUN dpkg -i google-chrome-stable_current_arm64.deb
#RUN wget https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip
#RUN unzip chromedriver_linux64.zip -d driver


#RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
#RUN bash -c "echo 'deb [arch=arm64v8] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list"
#RUN apt-get -y update
#RUN apt-get -y install google-chrome-stable

RUN apt-get update && apt-get install -y chromium python3 pip git python3-venv
    #&& git clone https://github.com/AnastasiiaDm/AQA_pytest.git /code \
    #&& cd /code \
    #&& python3 -m venv venv \
    #&& . venv/bin/activate \

#    && pip install -r requirements.txt \
#    && pytest seventeenth_hw/tests/ui_tests/test_main_page.py




#USER root
#
#RUN  apt-get update \
#     && apt-get install -y wget \
#     && rm -rf /var/lib/apt/lists/*
#
## Install Python and Chrome dependencies
#RUN \
#    echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/chrome.list && \
#    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
#    apt-get update && \
#    apt-get install -y xvfb google-chrome-stable jq && \
#    ln -sf /usr/bin/xvfb-chrome /usr/bin/google-chrome
#
#
## Set Chrome binary path
#ENV CHROME_BIN /usr/bin/google-chrome-stable
#ENV SERVER_URL "http://127.0.0.1:8111"
#
## Expose port for Chrome remote debugging
#EXPOSE 9222

# Set entrypoint to start the TeamCity agent
#ENTRYPOINT ["/run-agent.sh"]