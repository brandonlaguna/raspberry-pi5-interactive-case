import board
import neopixel
import time

NUM_PIXELS = 16
PIXEL_PIN = board.D18  # GPIO 18
BRIGHTNESS = 0.5

pixels = neopixel.NeoPixel(
    PIXEL_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=False
)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

for color in colors:
    pixels.fill(color)
    pixels.show()
    time.sleep(1)

pixels.fill((0, 0, 0))  # Apaga
pixels.show()
