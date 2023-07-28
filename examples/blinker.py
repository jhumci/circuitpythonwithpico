import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
        led.value = True
        time.sleep(1)
        led.value = False
        time.sleep(0.2)
        led.value = True
        time.sleep(0.2)
        led.value = False
        time.sleep(1)
        print("Sleep!!!")