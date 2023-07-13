import screen_brightness_control as sbc
import os

def setbrightness(value):
    sbc.set_brightness(value)
    os.system('cls')
