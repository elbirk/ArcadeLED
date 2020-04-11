import sys, getopt
from configparser import ConfigParser
import RPi.GPIO as LED
import os
# Adafruit NeoPixel libary
import board
import neopixel

# create an instance of ConfigParser class.
parser = ConfigParser()

# read and parse the configuration file.
parser.read(os.path.dirname(os.path.realpath(__file__))+'/Colors.ini')

# Curent rom name i empty all GPIO ON
RomName = ""
# LED or NeoPixel mode
LedMode = ""


# List with Button, PI GPIO pinout and holder for gpiozero
ArcadeButton = (('p1_coin', 22),
                ('p1_start', 18),
                ('p2_start', 23),
                ('p1_button1', 24),
                ('p1_button2', 25),
                ('p1_button3', 12),
                ('p1_button4', 16),
                ('p1_button5', 20),
                ('p1_button6', 21),
                ('p1_button7', 17),
                ('p1_button8', 27))


# Initialize Adafruit NeoPixel D10=GPIO10, Choose between GPIO pin 10, 12, 18, 22
pixels = neopixel.NeoPixel(board.D18, len(ArcadeButton)+1, pixel_order=neopixel.RGB)

# Colors
Palette = (('Black', (0, 0, 0)),
           ('Blue', (0, 0, 255)),
           ('Brown', (150, 75, 0)),
           ('Cyan', (0, 255, 255)),
           ('Green', (0, 255, 0)),
           ('Lime', (208, 255, 20)),
           ('Magenta', (255, 0, 255)),
           ('Orange', (230, 80, 0)),
           ('Purple', (160, 32, 240)),
           ('Red', (255, 0, 0)),
           ('Violet', (143, 0, 255)),
           ('White', (255, 255, 255)),
           ('Yellow', (255, 255, 0)))


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

unixOptions = "hr:m:"
gnuOptions = ["help", "RomName=", "Mode="]

try:
 arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
 print (str(err))
 sys.exit(2)

for currentArgument, currentValue in arguments:
 if currentArgument in ("-m", "--mode"):
  LedMode = currentValue #led or neopixel
 elif currentArgument in ("-h", "--help"):
  print("ArcadeLED.py -r romname")
 elif currentArgument in ("-r", "--RomName"):
  RomName = currentValue
# *** Command Line Arguments ***


# *** Button control ***
if RomName != "":
  GameButton = list(parser.items(RomName))
# *** NeoPixel ***
if LedMode == 'neopixel':
  if RomName != "":
    for ab in range(len(ArcadeButton)):
      if in_list(ArcadeButton[ab][0], GameButton) != -1 : 
        pixels[ab] = (Palette[in_list(GameButton[in_list(ArcadeButton[ab][0], GameButton)][1], Palette)][1])
        print(ArcadeButton[ab][0], GameButton[in_list(ArcadeButton[ab][0], GameButton)][1]) #Lite on button color
      else:
        print(ArcadeButton[ab][0], 'OFF') #Turn off not used buttons
        pixels[ab] = (0, 0, 0)  
# *** NeoPixel ***
# *** LED ***
else:    
  LED.setwarnings(False)
  LED.setmode(LED.BCM)
  if RomName == "": 
    for ab in range(len(ArcadeButton)):
      print(ArcadeButton[ab][0], 'ON', ArcadeButton[ab][1]) #Lite on All buttons
      LED.setup(ArcadeButton[ab][1], LED.OUT)
      LED.output(ArcadeButton[ab][1], LED.HIGH)
  else:
    for ab in range(len(ArcadeButton)):
      LED.setup(ArcadeButton[ab][1], LED.OUT)
      if in_list(ArcadeButton[ab][0], GameButton) != -1 : 
        print(ArcadeButton[ab][0], 'ON', ArcadeButton[ab][1]) #Lite on Rom specific buttons
        LED.output(ArcadeButton[ab][1], LED.HIGH)
      else:
        print(ArcadeButton[ab][0], 'OFF', ArcadeButton[ab][1]) #Lite on Rom specific buttons
        LED.output(ArcadeButton[ab][1], LED.LOW)
# *** LED ***
# *** Button control ***
