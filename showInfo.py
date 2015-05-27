import commands
import psutil

def showCurrentStation():
        STATION = commands.getoutput('mpc --format \"[%name%]\" | head -n 1')
        return STATION

def showCurrentArtist():
        SPLITTER = ' - '
        ARTIST = commands.getoutput('mpc --format \"[%artist%]\" | head -n 1')
        #ARTIST = ARTIST[:ARTIST.index(SPLITTER)]
        return ARTIST

def showCurrentTitle():
        SPLITTER = ' - '
        TITLE = commands.getoutput('mpc --format \"[%title%]\" | head -n 1')
        #TITLE = TITLE[TITLE.index(SPLITTER)+len(SPLITTER):]
        return TITLE
        
def showIP():
        IP_ADR = commands.getoutput("ip addr | grep 'state UP' -A2 | tail -n1 |$
        return IP_ADR

def showUptime():
        UPTIME = commands.getoutput("uptime | awk '{print $1}'")
        return UPTIME
        
def showVolume():
        VOLUME = commands.getoutput("mpc | head -n 2 | tail -n 1 | awk {'print $
        return VOLUME

def showCPU():
        return psutil.cpu_percent(interval=None)

def showRAM():
        RAM = psutil.virtual_memory()
        return RAM[2]

def showDiskUsageRoot():
        DU = psutil.disk_usage('/')
        return DU[3]

def showDiskUsageUSB():
        DU = psutil.disk_usage('/media/usb0')
        return DU[3]

def showDate():
        DATE = commands.getoutput('date +\"%d.%m.%y\"')
        return DATE

def showTime():
        TIME = commands.getoutput('date +\"%T\"')
        return TIME

def showTemp():
        TEMP = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp')
        TEMP = TEMP[5:-2]
        return TEMP



