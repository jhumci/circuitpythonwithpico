import lib.mywifi as mywifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import time
import socketpool
import wifi
import os

mywifi.connect_wifi()

# Setup a feed named 'photocell' for publishing to a feed
output_feed = "iot/{}/acceleration/test".format(os.getenv('MY_DEVICE_NAME'))

# Setup a feed named 'onoff' for subscribing to changes
onoff_feed = "iot/{}/actuator/onoff".format(os.getenv('MY_DEVICE_NAME'))


# Define callback methods which are called when events occur
# pylint: disable=unused-argument, redefined-outer-name
def connected(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print("Connected to {} Listening for topic changes on %s {}".format(os.getenv('MQTT_BROKER'), onoff_feed))
    # Subscribe to all changes on the onoff_feed.
    client.subscribe(onoff_feed)


def disconnected(client, userdata, rc):
    # This method is called when the client is disconnected
    print("Disconnected from MQTT-Broker!")


def message(client, topic, message):
    # This method is called when a topic the client is subscribed to
    # has a new message.
    print("New message on topic {0}: {1}".format(topic, message))

pool = socketpool.SocketPool(wifi.radio)

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker=os.getenv('MQTT_BROKER'),
    port = os.getenv('MQTT_PORT'),
    username=os.getenv('MQTT_USER'),
    password=os.getenv('MQTT_PASS'),
    socket_pool=pool,
    is_ssl=False
)


# Setup the callback methods above
mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message

# Connect the client to the MQTT broker.
print("Connecting to {}...".format(os.getenv('MQTT_BROKER')))
mqtt_client.connect()
print("Connected!"))

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
