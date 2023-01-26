FROM python:3.7-slim

WORKDIR /app

ADD ./app/common/utils/postgres.py /app/common/utils/postgres.py

ADD ./docker/pg-init-seeder /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["seeder.py"]
