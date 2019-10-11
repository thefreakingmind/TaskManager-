FROM ubuntu:16.04


RUN sudo apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /server

RUN pip install -r requirements.txt

COPY . /server

ENTRYPOINT [ "python" ]

CMD [ "server.py" ]
