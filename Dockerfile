FROM python:3.8.0-slim

ENV DBHOST=""
ENV DBUSER=""
ENV DBPASS=""
ENV DBNAME=""

COPY ./requirements.txt .

RUN pip install -r requirements.txt


#RUN pip install fastapi uvicorn

EXPOSE 14000

COPY . .

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "14000"]
