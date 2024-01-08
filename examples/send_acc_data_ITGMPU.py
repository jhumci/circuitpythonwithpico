# Wenn Bus keine Geräte findet, Widerstand prüfen!
import time
import board
import busio
import adafruit_mpu6050
import os
import mywifi
import mymqtt

output_feed_x = "iot/{}/acceleration/x".format(os.getenv('MY_DEVICE_NAME'))
output_feed_y = "iot/{}/acceleration/y".format(os.getenv('MY_DEVICE_NAME'))
output_feed_z = "iot/{}/acceleration/z".format(os.getenv('MY_DEVICE_NAME'))

mywifi.connect_wifi()
mqtt_client = mymqtt.connect_mqtt()

i2c = busio.I2C(scl=board.GP15, sda=board.GP14)

mpu = adafruit_mpu6050.MPU6050(i2c)


while True:
    # Poll the message queue
    #mqtt_client.loop()

    print(mpu.acceleration)
    
    # Send a new message
    mqtt_client.publish(output_feed_x, mpu.acceleration[0])
    mqtt_client.publish(output_feed_y, mpu.acceleration[1])
    mqtt_client.publish(output_feed_z, mpu.acceleration[2])
    time.sleep(1)
