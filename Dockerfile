FROM python:3.9



ENV PYHTONDONTTWRITEBYTECODE 1
ENV PYTHONUNBYFFERED 1


WORKDIR /app


COPY requirements.txt .
RUN pip install --no--cache-dir -r requirements.txt


COPY . /app/


CMD['python', 'manage.py', 'runserver', '0.0.0.0:8000']