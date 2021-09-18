FROM python:3.8.0-slim

RUN mkdir /home/code
WORKDIR /home/code

COPY ./requirements.txt .

RUN pip install -r requirements.txt


#RUN pip install fastapi uvicorn

COPY . .

#CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "14000"]