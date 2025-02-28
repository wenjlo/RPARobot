FROM python:3.11.9
RUN apt-get update && apt-get -y install cron vim
WORKDIR /app
ADD . /app

RUN apt-get update
RUN apt-get install -y wget
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable

RUN pip install -r requirements.txt

#CMD ["python","/app/main.py"]
#CMD ["cron","&&","tail","-f","/var/log/cron.log"]