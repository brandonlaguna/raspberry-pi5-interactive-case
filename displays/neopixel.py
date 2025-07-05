import board
import neopixel
import time

NUM_PIXELS = 16
PIXEL_PIN = board.D18
BRIGHTNESS = 0.5

pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=False)

# Secuencia básica de colores
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # rojo, verde, azul

for color in colors:
    for i in range(NUM_PIXELS):
        pixels[i] = color
    pixels.show()
    time.sleep(1)

# Apaga todos
pixels.fill((0, 0, 0))
pixels.show()