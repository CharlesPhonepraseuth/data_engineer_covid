FROM python:3.7-slim

WORKDIR /code

ADD ./app/common/utils /code/common/utils
ADD ./app/dashboard /code/dashboard
ADD ./app/__init__.py /code/__init__.py

ADD ./docker/dashboard /code
RUN pip install -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH/code

ENTRYPOINT ["python"]
CMD ["dashboard/index.py"]
