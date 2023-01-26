FROM python:3.7-slim

WORKDIR /app

ADD ./app/common/utils/elasticsearch.py /app/common/utils/elasticsearch.py

ADD ./docker/es-init-seeder /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["seeder.py"]
