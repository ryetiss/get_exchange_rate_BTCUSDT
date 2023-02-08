#Docker file for automating the exchange rates check
FROM ubuntu:20.04

WORKDIR /app

COPY btcusdt-script.py .
COPY flask-script.py .

RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --no-cache-dir requests
RUN pip3 install --no-cache-dir flask
RUN nohup python3 btcusdt-script.py &

EXPOSE 80

CMD ["python3", "flask-script.py"]
