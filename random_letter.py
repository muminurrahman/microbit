from microbit import display, accelerometer, sleep
import random

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXZ")

while True:
    if accelerometer.was_gesture("shake"):
        letter = random.choice(alphabet)
        display.clear()
        sleep(1000)
        display.show(letter)
