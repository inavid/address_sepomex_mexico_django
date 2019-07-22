FROM python:3.6
ARG ENV=dev

RUN apt-get update && apt-get install -y gettext libgettextpo-dev
RUN mkdir /code
WORKDIR /code
ADD ./requirements /code/requirements
RUN pip install --upgrade pip
RUN pip install -Ur requirements/$ENV.txt
