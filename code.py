# Wenn Bus keine Geräte findet, Widerstand prüfen!
import time
import board
import busio
import adafruit_adxl34x
import os
import lib.mywifi as mywifi
import lib.mymqtt as mymqtt

output_feed_x = "iot/{}/acceleration/x".format(os.getenv('MY_DEVICE_NAME'))
output_feed_y = "iot/{}/acceleration/y".format(os.getenv('MY_DEVICE_NAME'))
output_feed_z = "iot/{}/acceleration/z".format(os.getenv('MY_DEVICE_NAME'))

mywifi.connect_wifi()
mqtt_client = mymqtt.connect_mqtt()

i2c = busio.I2C(scl=board.GP15, sda=board.GP14)

accelerometer = adafruit_adxl34x.ADXL345(i2c)


while True:
    # Poll the message queue
    #mqtt_client.loop()

    # Send a new message
    mqtt_client.publish(output_feed_x, accelerometer.acceleration[0])
    mqtt_client.publish(output_feed_y, accelerometer.acceleration[1])
    mqtt_client.publish(output_feed_z, accelerometer.acceleration[2])
    time.sleep(1)
