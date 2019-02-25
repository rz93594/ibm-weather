FROM python:3

COPY requirements.txt /
COPY credentials.py /
COPY mount_mediacenter.sh /

ADD get_current_weather.py /

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y cifs-utils && apt-get clean
RUN mkdir /tmp/media

#ENTRYPOINT "/mount_mediacenter.sh" && "/usr/local/bin/python /get_current_weather.py"
CMD [ "/usr/local/bin/python", "/get_current_weather.py" ]

