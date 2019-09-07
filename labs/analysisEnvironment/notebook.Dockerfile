FROM jupyter/all-spark-notebook:82d1d0bf0867
MAINTAINER geoHeil <georg.heiler@csh.ac.at>

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
