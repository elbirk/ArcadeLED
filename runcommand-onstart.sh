#!/usr/bin/bash

if [ -z "$3" ]; then
  exit 0
fi

rom_name="$(basename "$3")"
rom="${rom_name%.*}"

# Turn on the relevant LEDs for this game.
python3 /home/pi/RetroPie/ArcadeLED/ArcadeLED.py -r "$rom" 
