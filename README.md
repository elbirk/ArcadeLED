# ArcadeLED
Retropie python3 script for rom specific button light on Raspberry PI and RetroPie.

Python3 script that reads Colors.ini and turn on the GPIO pins of Raspberry PI, when the specific games is launched.
The Colors.ini file includes many MAME games, made by Kevin Jonas (SirPoonga) http://controls.arcadecontrols.com/

To change the GPIO pin numbers and Arcade buttons in you cabinet, edit ArcadeLED.py

Without parameter ArcadeLED will turn on all your led buttons.
Calling ArcadeLED.py without parameter, turns on all led buttons
Calling ArcadeLED.py -r OFF, turns off alle led buttons
Calling ArcadeLED.py -r bombjack turn on alle buttons used by Bomb Jack

the script runcommand-onstart.sh is called from RetroPie and calls ArcadeLED.py -r romname called.
the script runcommand-onend.sh -r OFF

copy ArcadeLED forlder to RetroPie
copy runcommand-onstart.sh and runcommand-onend.sh to /opt/retropie/configs/all


Run on Raspberry PI:  
sudo apt-get install python3 (Installs Python 3)  
sudo apt-get install rpi.gpio (installs rpi.gpio, used for controlling GPIO ports)


Because you cannot run the buttons direct from Raspberry PI, you ned at Darlington Transistor Array.
I uses 2 pices of ULN2803A boards. 
https://www.ebay.com/itm/ULN2803A-Darlington-Tube-High-Pressure-Large-Current-Drive/112571472802?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2057872.m2749.l2649
