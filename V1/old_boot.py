import time
from machine import Pin, SPI
import gc9a01
import romand

def main():
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

    tft.init()
    tft.fill(gc9a01.WHITE)
    
    while True:
        tft.jpg("11d.jpg", 30, 20, gc9a01.FAST)
        tft.draw(romand, "Enrique", 130, 70, gc9a01.BLUE)
        tft.text(romand, "Enrique", 120, 50, gc9a01.BLUE)

        tft.jpg("logo.jpg", 55, 130, gc9a01.FAST)
        tft.draw(romand, "Gamboa", 130, 155, gc9a01.BLACK)
        
        time.sleep(1)

main()

