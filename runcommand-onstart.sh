#!/usr/bin/bash

if [ -z "$3" ]; then
  exit 0
fi

rom_name="$(basename "$3")"
rom="${rom_name%.*}"

# Turn on the relevant neopixel for this game.
sudo python3 /home/pi/RetroPie/ArcadeLED/ArcadeLED.py -r "$rom" -m neopixel

# Turn on the relevant led for this game.
#sudo python3 /home/pi/RetroPie/ArcadeLED/ArcadeLED.py -r "$rom"
