from microbit import Image, accelerometer, display, sleep
import random

one = Image("00000:"
            "00000:"
            "00900:"
            "00000:"
            "00000")

two = Image("90000:"
            "00000:"
            "00000:"
            "00000:"
            "00009")

two2 = Image("00009:"
            "00000:"
            "00000:"
            "00000:"
            "90000")

three = Image("90000:"
              "00000:"
              "00900:"
              "00000:"
              "00009")

three2 = Image("00009:"
              "00000:"
              "00900:"
              "00000:"
              "90000")

four = Image("90009:"
            "00000:"
            "00000:"
            "00000:"
            "90009")

five = Image("90009:"
            "00000:"
            "00900:"
            "00000:"
            "90009")

six = Image("90009:"
            "00000:"
            "90009:"
            "00000:"
            "90009")

six2 = Image("90909:"
            "00000:"
            "00000:"
            "00000:"
            "90909")

dice = [one, one, two, two2, three, three2, four, four, five, five, six, six2]

while True:
    if accelerometer.was_gesture("shake"):
        roll = random.choice(dice)
        display.clear()
        sleep(1000)
        display.show(roll)
