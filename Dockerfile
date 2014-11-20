FROM resin/rpi-raspbian:wheezy

RUN apt-get update

RUN apt-get upgrade -y

RUN apt-get install -y python wget build-essential python-dev python-pip

RUN pip install RPi.Gpio

ADD gpio_example.py /App/

RUN echo 'python /App/gpio_example.py && tail -f /App/gpio.log' > /start
RUN chmod +x /start