# Basic GPIO with Python on Resin
This is a basic example of GPIO control on the Rasperry Pi using Python

We use the GPIO board pin mapping and we also need few LEDs on two sets of GPIO pin:

Set A: 3,5,7,8,10,11,12,13,15 (pin number)
Set B: 16.18,19,21,22,23,24,26 (pin number)

In this example, the LEDs on two sets will be switched between on and off after one sec. If set A is on then set B is off and vice versa.

All you need to do is :
* Create a new application on the [resin dashboard](https://dashboard.resin.io) (more information: [Getting Started](https://docs.resin.io/raspberrypi3/python/getting-started/))
* Clone this repo: `git clone https://github.com/resin-io-projects/resin-rpi-gpio-sample-with-python.git`
* Connect LEDs to both sets of pins
* Copy the git command from the top right of the resin dashboard application, the one starting `git remote add ...` and run it in the cloned repository
* Run `git push resin master` and let the code compile and synchronise with your connected devices
* Enjoy your resinified LEDs!