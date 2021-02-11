FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /NewsSite
WORKDIR /NewsSite
COPY requirements.txt /NewsSite/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /NewsSite/