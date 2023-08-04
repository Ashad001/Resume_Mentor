FROM python:3.8

RUN pip install --upgrade pip
WORKDIR /resume-mentor

COPY requirements.txt .
COPY ./src ./src
RUN pip install -r requirements.txt
CMD [ "python", "./src/main.py" ]
