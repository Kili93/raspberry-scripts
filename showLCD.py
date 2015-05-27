import Adafruit_CharLCD as LCD
import showInfo
import commands
import time

lcd = LCD.Adafruit_CharLCDPlate()
lcd.set_backlight(0)
lcd.enable_display(0)

LINE1 = ''
LINE2 = ''
ENABLE_LCD = 0
STATS = 0
SITE = 4
CURRENT = ''
STOP = 0
while STOP == 0:
        if lcd.is_pressed(LCD.RIGHT):
                STOP = 1
        CURRENT = commands.getoutput('mpc current')
        if CURRENT is not None:
                lcd.enable_display(1)
                lcd.set_backlight(1)
                LINE1 = showInfo.showCurrentArtist()
                LINE2 = showInfo.showCurrentTitle()
        if lcd.is_pressed(LCD.SELECT):
                if CURRENT is not None:
                        commands.getoutput('mpc stop')
                else:
                        commands.getoutput('mpc play')
        if STATS == 1:
                LINE1 = showInfo.showIP()
                LINE2 = showInfo.showUptime()
        if STATS == 2:
                LINE1 = 'CPU :' +str(showInfo.showCPU())+'%'
                LINE2 = 'RAM :' +str(showInfo.showRAM())+'%'
        if STATS == 3:
                LINE1 = 'root: ' +str(showInfo.showDiskUsageRoot())+'%'
                LINE2 = 'USB : ' +str(showInfo.showDiskUsageUSB())+'%'
        if STATS == 4:
                LINE1 = 'Datum :' +showInfo.showDate()
                LINE2 = 'Zeit  :' +showInfo.showTime()
        if STATS == 5:
                MESSAGE = 'Temperatur      :\n' +showInfo.showTemp()+' C'
        if lcd.is_pressed(LCD.UP):
                //Volume up
        if lcd.is_pressed(LCD.DOWN):
                //Volume Down
        if lcd.is_pressed(LCD.LEFT):
                if STATS > 5:
                        STATS = 0
                else:
                        STATS = STATS +1
       while len(LINE1) < 16:
                LINE1 = LINE1 + ' '
        while len(LINE2) < 16:
                LINE2 = LINE2 + ' '
        lcd.message(LINE1 + '\n' + LINE2)

lcd.set_backlight(0)
lcd.enable_display(0)
