# ArcadeLED Normal led or neopixel
Retropie python3 script for rom specific button light on Raspberry PI and RetroPie.  
Python3 script that reads Colors.ini and turn on the game specific buttons launching a game.  
  
The Colors.ini file includes many MAME games, made by Kevin Jonas (SirPoonga) http://controls.arcadecontrols.com/  
To change the GPIO pin numbers and Arcade buttons in your cabinet, edit ArcadeLED.py  
Normal LED buttons parameters:  
python3 ArcadeLED.py -r bombjack  
Neopixel LED buttons parameters:  
python3 ArcadeLED.py -m neopixel -r bombjack  
  
Installaton  
copy ArcadeLED folder to /home/pi/RetroPie  
copy runcommand-onstart.sh and runcommand-onend.sh to /opt/retropie/configs/all  
Edit runcommand-onstart.sh and runcommand-onend.sh for your configuration  
  
Run on Raspberry PI(Retropie-Buster):  
sudo apt-get install python3  
sudo apt install python3-pip  
sudo pip3 install RPI.GPIO  
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel  
  
Neopixel can be connected direct to Raspberry PI.  
Normal LED you can use a Darlington Transistor Array to connect the Leds.  
  
I uses 2 pices of ULN2803A boards.  
https://www.ebay.com/itm/ULN2803A-Darlington-Tube-High-Pressure-Large-Current-Drive/112571472802?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2057872.m2749.l2649  


