FROM python:3.10

RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /web
COPY requirements.txt .

RUN pip install -U pip 
RUN pip install -r requirements.txt

COPY . /web/
EXPOSE 8000

CMD [ "gunicorn","schoolsystem.wsgi",":8000" ]