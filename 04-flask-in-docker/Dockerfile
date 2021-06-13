FROM python:3.7-alpine
LABEL maintainer="iamcjf@gmail.com"

WORKDIR /app
COPY codes /app

# install python required packages
COPY requirements.txt /app
RUN pip install -r  /app/requirements.txt
RUN rm -rf /tmp/*

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh


ENTRYPOINT [ "/sbin/entrypoint.sh" ]