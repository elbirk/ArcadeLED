import sys, getopt
from configparser import ConfigParser
import RPi.GPIO as LED
import os

# create an instance of ConfigParser class.
parser = ConfigParser()

# read and parse the configuration file.
parser.read(os.path.dirname(os.path.realpath(__file__))+'/Colors.ini')

# List with Button, PI GPIO pinout and holder for gpiozero
ArcadeButton = [['p1_coin', 22], ['p1_start', 18], ['p2_start', 23], ['p1_button1', 24], ['p1_button2', 25], ['p1_button3', 12], ['p1_button4', 16], ['p1_button5', 20], ['p1_button6', 21], ['p1_button7', 17], ['p1_button8', 27]]

# Curent rom name i empty all GPIO ON
RomName = ""


# function in_list
def in_list(c, classes):
    for i, sublist in enumerate(classes):
        if c in sublist:
            return i
    return -1
# function in_list


# *** Command Line Arguments ***
fullCmdArguments = sys.argv
argumentList = fullCmdArguments[1:]

unixOptions = "hr:f"
gnuOptions = ["help", "RomName=", "Future="]

try:
 arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
 print (str(err))
 sys.exit(2)

for currentArgument, currentValue in arguments:
 if currentArgument in ("-f", "--future"):
  print("future use")
 elif currentArgument in ("-h", "--help"):
  print("ArcadeLED.py -r romname")
 elif currentArgument in ("-r", "--RomName"):
  RomName = currentValue
# *** Command Line Arguments ***


# *** Button control ***
LED.setwarnings(False)
LED.setmode(LED.BCM)
if RomName == "": 
  for ab in range(len(ArcadeButton)):
    print(ArcadeButton[ab][1], 'ON') #Lite on All specific buttons
    LED.setup(ArcadeButton[ab][1], LED.OUT)
    LED.output(ArcadeButton[ab][1], LED.HIGH)
else:
  GameButton = list(parser.items(RomName))
  for ab in range(len(ArcadeButton)):
      LED.setup(ArcadeButton[ab][1], LED.OUT)
      if in_list(ArcadeButton[ab][0], GameButton) != -1 : 
        print(ArcadeButton[ab][1], 'ON') #Lite on Rom specific buttons
        LED.output(ArcadeButton[ab][1], LED.HIGH)
      else:
        print(ArcadeButton[ab][1], 'OFF') #Lite on Rom specific buttons
        LED.output(ArcadeButton[ab][1], LED.LOW)
# *** Button control ***




