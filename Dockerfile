FROM python:3.11

RUN apt-get update && apt-get install -y netcat-traditional

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code

ENTRYPOINT ["/code/entrypoint.sh"]

