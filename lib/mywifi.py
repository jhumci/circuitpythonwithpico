import wifi as wifi
import os


def connect_wifi():
    print(f"Connecting to {os.getenv('CIRCUITPY_WIFI_SSID')}")
    wifi.radio.connect(
        os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD")
    )
    print(f"Connected to {os.getenv('CIRCUITPY_WIFI_SSID')}!")

#connect_wifi()