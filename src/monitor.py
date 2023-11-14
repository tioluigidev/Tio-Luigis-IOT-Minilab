import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI
import RPi.GPIO as gpio
from subprocess import call
from enum import Enum
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

DISPLAYS_DC = 23
DISPLAY1_RST = 20
DISPLAY2_RST = 21
DISPLAY1_LCD = 1
DISPLAY2_LCD = 25
BTN_RESET = 15
BTN_OFF = 18

display1 = LCD.PCD8544(DISPLAYS_DC, DISPLAY1_RST, spi=SPI.SpiDev(0, 0, max_speed_hz=4000000))
display2 = LCD.PCD8544(DISPLAYS_DC, DISPLAY2_RST, spi=SPI.SpiDev(0, 1, max_speed_hz=4000000))

display1.begin(contrast=40)
display2.begin(contrast=58)

image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
draw = ImageDraw.Draw(image)


draw.rectangle((0, 0, LCD.LCDWIDTH, LCD.LCDHEIGHT), outline=255, fill=255)
draw.text ((0,0), 'CPU Display')
draw.text ((0,10), 'Hello World!')

display1.image(image)
display1.display()


draw.rectangle((0, 0, LCD.LCDWIDTH, LCD.LCDHEIGHT), outline=255, fill=255)
draw.text((0,0), 'App Display')
draw.text((0,10), 'Hello World!')

display2.image(image)
display2.display()



gpio.setmode(gpio.BCM)

gpio.setup(BTN_RESET, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(BTN_OFF, gpio.IN, pull_up_down = gpio.PUD_DOWN)

gpio.setup(DISPLAY1_LCD, gpio.OUT)
gpio.setup(DISPLAY2_LCD, gpio.OUT)

gpio.output(DISPLAY1_LCD, 0)
gpio.output(DISPLAY2_LCD, 0)

while (True):
  if gpio.input(BTN_RESET):
    print('RESET')
    call('sudo reboot', shell=True)
    break
  if gpio.input(BTN_OFF):
    print('OFF')
    call('sudo shutdown -h now', shell=True)
    