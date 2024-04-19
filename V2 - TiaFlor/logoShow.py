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
    
    # Assuming logo.jpg is 100x100 pixels
    image_width = 50
    image_height = 50
    x = (240 - image_width) // 2
    y = (240 - image_height) // 2

    while True:
        tft.jpg("logo.jpg", x, y, gc9a01.FAST)
        time.sleep(1)

main()

