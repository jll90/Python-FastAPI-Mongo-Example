FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt-get update

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0"]
