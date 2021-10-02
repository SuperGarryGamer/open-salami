import time
import uasyncio
from machine import Pin
import driver

FRAMERATE = 30

BOUNCE_DELAY = 0.05
DISPLAY = driver.Display(0x3C)

last_bounce_time = 0

DISPLAY.draw_bitmap(0, 0, '/title.pbm')

pointer_spr = driver.Sprite(DISPLAY, 30, 42)
pointer_spr.load_from_pbm('/pointer.pbm')
DISPLAY.on()

A_PIN = Pin(0, Pin.IN)
B_PIN = Pin(1, Pin.IN)

buttons = [False, False]

# def get_button_inputs():
#     buttons_old = buttons
#     buttons = [A_PIN.value(), B_PIN.value()]

async def draw_disp():
    DISPLAY.draw()

async def main():
    while True:
        print(A_PIN.value())
        uasyncio.create_task(draw_disp())
        time.sleep(1/FRAMERATE)

uasyncio.run(main())