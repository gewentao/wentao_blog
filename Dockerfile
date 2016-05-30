FROM python:2.7
MAINTAINER Ted Ge <gewentao@outlook.com>
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

ADD run.sh /code/
RUN chmod 777 run.sh
EXPOSE 80

CMD ["/bin/sh", "run.sh"]
