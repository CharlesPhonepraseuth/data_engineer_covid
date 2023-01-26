FROM python:3.7-slim

USER root

RUN apt-get update

ADD ./docker/notebook /code
RUN pip install -r code/requirements.txt

WORKDIR /home/jupyter

ENTRYPOINT ["jupyter", "notebook", "--allow-root", "--ip=0.0.0.0"]
