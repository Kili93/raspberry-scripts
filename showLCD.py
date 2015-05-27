import Adafruit_CharLCD as LCD
import showInfo
import commands
import time

lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_backlight(1)
lcd.enable_display(1)

LINE1 = ''
LINE2 = ''
ENABLE_LCD = 0
SITE = 4
CURRENT = ''
while (SITE < 8):
        CURRENT = commands.getoutput('mpc current')
        lcd.home()
        if SITE == 0:
                lcd.set_backlight(0)
        if SITE > 0:
                lcd.set_backlight(1)
        if CURRENT is not None:
                SITE = 2
        if SITE == 1:
                MESSAGE = 'Station:        \n' +showInfo.showCurrentStation()
        if SITE == 2:
                LINE1 = showInfo.showCurrentArtist()
                LINE2 = showInfo.showCurrentTitle()
        if SITE == 3:
                LINE1 = 'Volume'
                LINE2 = showInfo.showVolume()
        if SITE == 4:
                LINE1 = showInfo.showIP()
                LINE2 = showInfo.showUptime()
        if SITE == 5:
                LINE1 = 'CPU :' +str(showInfo.showCPU())+'%'
                LINE2 = 'RAM :' +str(showInfo.showRAM())+'%'
        if SITE == 6:
                LINE1 = 'root: ' +str(showInfo.showDiskUsageRoot())+'%'
                LINE2 = 'USB : ' +str(showInfo.showDiskUsageUSB())+'%'
        if SITE == 7:
                LINE1 = 'Datum :' +showInfo.showDate()
                LINE2 = 'Zeit  :' +showInfo.showTime()
        if SITE == 13:
                MESSAGE = 'Temperatur      :\n' +showInfo.showTemp()+' C'
        if lcd.is_pressed(LCD.UP):
                SITE = SITE + 1
        if lcd.is_pressed(LCD.DOWN):
                SITE = SITE - 1
       while len(LINE1) < 16:
                LINE1 = LINE1 + ' '
        while len(LINE2) < 16:
                LINE2 = LINE2 + ' '
        lcd.message(LINE1 + '\n' + LINE2)

lcd.set_backlight(0)
lcd.enable_display(0)
