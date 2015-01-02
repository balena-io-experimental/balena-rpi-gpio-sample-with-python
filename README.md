# Basic GPIO with Python on Resin
This is a basic example of GPIO control on the Rasperry Pi using Python

We use the GPIO board pin mapping and we also need few LEDs on two sets of GPIO pin:

Set A: 3,5,7,8,10,11,12,13,15 (pin number)
Set B: 16.18,19,21,22,23,24,26 (pin number)

In this example, the LEDs on two sets will be switched between on and off after one sec. If set A is on then set B is off and vice versa.

All you need to do is :

* clone this repo locally  and cd into the folder.
* connect some LEDs to two pin sets
* add the resin remote repo with `git remote add resin git@git.resin.io:myGithubName/myResinAppName.git` , with the correct github and app name, or just copy if from the top right hand corner of your device dashboard on resin.io.
* now just `git push resin master` wait a minute or so for the code to upload and start.
* enjoy the all the LED goodness...