from microbit import accelerometer, display, sleep
import random

coin = ["H", "T"]

while True:
    if accelerometer.was_gesture("shake"):
        flip = random.choice(coin)
        display.clear()
        sleep(1000)
        display.show(flip)
