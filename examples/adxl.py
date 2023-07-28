# Wenn Bus keine Geräte findet, Widerstand prüfen!
import time
import board
import busio
import adafruit_adxl34x

i2c = busio.I2C(scl=board.GP15, sda=board.GP14)

accelerometer = adafruit_adxl34x.ADXL345(i2c)

while True:
    print("Read!")
    print("%f %f %f" % accelerometer.acceleration)
    time.sleep(0.2)