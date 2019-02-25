FROM python:3
VOLUME D://temp//docker-temp
COPY requirements.txt /
COPY credentials.py /
ADD get_current_weather.py /
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y cifs-utils
RUN mkdir /tmp/media
RUN mount -t cifs //mediacenter/Temp /tmp/media -o username=tv,password=


CMD [ "python", "./get_current_weather.py" ]

