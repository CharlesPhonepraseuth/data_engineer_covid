FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD ./app/common/utils /code/common/utils
ADD ./app/fastapi /code/app
ADD ./app/__init__.py /code/__init__.py

COPY ./docker/fastapi/requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

WORKDIR /code/app

ENV PYTHONPATH=$PYTHONPATH/code

CMD ["uvicorn", "router:app", "--reload",  "--host", "0.0.0.0"]
