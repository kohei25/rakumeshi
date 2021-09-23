FROM python:3.8-slim-buster

WORKDIR /var/www

COPY . /var/www/

RUN pip3 install flaskr-1.0.0-py3-none-any.whl

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
