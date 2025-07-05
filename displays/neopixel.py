import time
from rpi_ws281x import PixelStrip, Color

# Configuración de LEDs
LED_COUNT = 16         # Número de LEDs
LED_PIN = 18           # GPIO 18 (PWM)
LED_FREQ_HZ = 800000   # Frecuencia típica WS2812
LED_DMA = 10
LED_BRIGHTNESS = 128
LED_INVERT = False
LED_CHANNEL = 0

# Inicializa la tira
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

# Efecto de color secuencial
colors = [Color(255, 0, 0), Color(0, 255, 0), Color(0, 0, 255)]

for color in colors:
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    time.sleep(1)

# Apaga todo
strip.fill(Color(0, 0, 0))
strip.show()
