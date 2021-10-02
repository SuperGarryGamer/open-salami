import time
import driver

DISPLAY = driver.Display(0x3C)

DISPLAY.draw_bitmap(0, 0, '/title.pbm')

pointer_spr = driver.Sprite(DISPLAY, 30, 42)
pointer_spr.load_from_pbm('/pointer.pbm')
DISPLAY.on()

while True:
    pointer_spr.draw()
    DISPLAY.draw()
    time.sleep(0.25)
    print('a')
    DISPLAY.clear_area(30, 42, 8, 8)
    DISPLAY.draw()
    time.sleep(0.25)
    print('b')