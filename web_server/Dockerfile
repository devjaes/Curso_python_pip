FROM python:3.10

WORKDIR /web_server
COPY requirements.txt /web_server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /web_server/requirements.txt

COPY . /web_server/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]