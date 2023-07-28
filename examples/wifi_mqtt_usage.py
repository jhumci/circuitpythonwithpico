import lib.mywifi as mywifi
import lib.mymqtt as mymqtt
import time
import os

output_feed = "iot/{}/acceleration/testvalue".format(os.getenv('MY_DEVICE_NAME'))

mywifi.connect_wifi()
mqtt_client = mymqtt.connect_mqtt()

test_val = 0
while True:
    # Poll the message queue
    mqtt_client.loop()

    # Send a new message
    print("Sending value: %d..." % test_val)
    mqtt_client.publish(output_feed, test_val)
    print("Sent!")
    test_val += 1
    time.sleep(1)