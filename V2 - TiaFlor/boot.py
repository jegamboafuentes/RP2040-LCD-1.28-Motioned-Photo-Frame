from machine import Pin, SPI, I2C
import time
import gc9a01
from sensors import QMI8658
import random  # Import the random module

# Corrected setup for QMI8658 gyroscope using individual SDA and SCL pin numbers
I2C_SDA = 6
I2C_SCL = 7

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
        rotation=2)

    tft.init()
    tft.fill(gc9a01.WHITE)

    # Initialize the QMI8658 sensor with SDA and SCL pin numbers
    qmi8658 = QMI8658(I2C_SDA, I2C_SCL)

    image_paths = ["logo230.jpg","1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg"]
    current_image_path = random.choice(image_paths)

    image_width = 230
    image_height = 230
    x = (240 - image_width) // 2
    y = (240 - image_height) // 2

    # Initialize the timer
    last_change_time = time.time()

    def read_gyroscope(acc_threshold=1, gyro_threshold=20):
        """
        Check for significant movement using the gyroscope and accelerometer.
        Returns True if significant movement is detected, False otherwise.
        """
        xyz = qmi8658.Read_XYZ()
        acc_magnitude = (xyz[0]**2 + xyz[1]**2 + xyz[2]**2)**0.5
        gyro_magnitude = (xyz[3]**2 + xyz[4]**2 + xyz[5]**2)**0.5

        print(f"Acc: {acc_magnitude}, Gyro: {gyro_magnitude}")

        if acc_magnitude < 1 or acc_magnitude > 1.3:
            return True
        return False

    while True:
        current_time = time.time()
        if read_gyroscope() or (current_time - last_change_time >= 11):
            # Keep selecting a new image path until it's different from the current one
            new_image_path = current_image_path
            while new_image_path == current_image_path:
                new_image_path = random.choice(image_paths)
            current_image_path = new_image_path
            tft.fill(gc9a01.WHITE)
            tft.jpg(current_image_path, x, y, gc9a01.FAST)
            last_change_time = current_time  # Reset the timer after changing the image

        time.sleep(1)

main()
