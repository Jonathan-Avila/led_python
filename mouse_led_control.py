#!/usr/bin/env python3

from gpiozero import LED
from time import sleep
from pynput.mouse import Listener

MouseListener = Listener

led = LED(17)
def on_click(x, y, button, pressed):
    if pressed:
    	led.on()

    if not pressed:
        led.off()



print ('Program is starting ... ')
           # define LED pin according to BCM Numbering
# led = LED("J8:11")     # BOARD Numbering
'''
# pins numbering, the following lines are all equivalent
led = LED("GPIO17")     # BCM
led = LED("BCM17")      # BCM
led = LED("BOARD11")    # BOARD
led = LED("WPI0")       # WiringPi
led = LED("J8:11")      # BOARD
'''


with MouseListener(on_click=on_click) as mouse_listener:
    mouse_listener.join()
