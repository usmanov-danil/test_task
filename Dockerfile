FROM python:3.8.2

ENV PYTHONUNBUFFERED 1

WORKDIR /app/

RUN sed -i '/jessie-updates/d' /etc/apt/sources.list && \
    apt-get update && apt-get install -y --no-install-recommends \
    gettext gdal-bin jpegoptim optipng pngquant gifsicle && \
    apt-get clean

COPY requirements.txt .
RUN pip install -r requirements.txt

#COPY deploy/ deploy/
#RUN chmod +x deploy/wait-for-it.sh
#RUN ls

CMD python manage.py migrate
