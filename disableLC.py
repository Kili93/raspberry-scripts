#!/usr/bin/python
# Example using a character LCD plate.

import Adafruit_CharLCD as LCD


# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_backlight(0)
lcd.enable_display(0)
