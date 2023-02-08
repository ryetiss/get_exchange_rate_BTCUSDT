# Getting the exchange rates of BTCUSDT Script

This is the example of Docker container app for Python script for getting the exchange rates of BTCUSDT crypto currency.

#### Build Docker image

    $ docker build -t script:node .

#### Create Docker container with existing image

    $ docker run -d --name script-node --hostname script-node script:node

#### Check Docker container

    $ docker exec -it script-node bash

#### if the nohup command didn't run, use this command in the docker container bash:

    root@script-node:/app# nohup python3 binance-script.py &
    
#### Check the result

    $ curl http://$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' script-node)
