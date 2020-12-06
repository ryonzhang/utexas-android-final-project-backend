FROM python:3.8-slim
LABEL maintainer="ruiyang.zhang@utexas.edu"
ENV PROJECT_ROOT .
WORKDIR $PROJECT_ROOT
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:8000 --insecure