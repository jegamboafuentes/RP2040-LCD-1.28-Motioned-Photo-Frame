'''
alien.py

    Randomly draw a jpg using the fast method on a GC9A01 display
    connected to a Raspberry Pi Pico.

    Pico Pin   Display
    =========  =======
    14 (GP10)  BL
    15 (GP11)  RST
    16 (GP12)  DC
    17 (GP13)  CS
    18 (GND)   GND
    19 (GP14)  CLK
    20 (GP15)  DIN

    The alien.jpg is from the Erik Flowers Weather Icons available from
    https://github.com/erikflowers/weather-icons and is licensed under
    SIL OFL 1.1

    It was was converted from the wi-alien.svg icon using
    ImageMagick's convert utility:

    convert wi-alien.svg -type TrueColor alien.jpg
'''

import gc
import random
from machine import Pin, SPI
import gc9a01

gc.enable()
gc.collect()


def main():
    '''
    Decode and draw jpg on display
    '''
    spi = SPI(1, baudrate=60000000, sck=Pin(10), mosi=Pin(11))
    tft = gc9a01.GC9A01(
        spi,
        240,
        240,
        reset=Pin(12, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        dc=Pin(8, Pin.OUT),
        backlight=Pin(25, Pin.OUT),
        rotation=0)

    # enable display and clear screen
    tft.init()

    # display jpg in random locations
    while True:
        tft.rotation(random.randint(0, 4))
        tft.jpg(
            "logo.jpg",
            random.randint(0, tft.width() - 30),
            random.randint(0, tft.height() - 30),
            gc9a01.FAST)


main()
