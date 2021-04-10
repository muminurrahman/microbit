from microbit import accelerometer, display, sleep
import random

numbers = list(range(10))

while True:
    if accelerometer.was_gesture("shake"):
        number = random.choice(numbers)
        display.clear()
        sleep(1000)
        display.show(number)
