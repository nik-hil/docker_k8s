FROM python:3.7-alpine
#ADD . /usr/src/app
#WORKDIR /usr/src/app
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
# EXPOSE 8000
#CMD ["python3", "manage.py", "runserver", "0:8000" ]
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD python manage.py runserver 0.0.0.0:8000
