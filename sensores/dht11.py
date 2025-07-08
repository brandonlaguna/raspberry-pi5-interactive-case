from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from PIL import ImageFont
import Adafruit_DHT
import time

# --- Configuración del sensor DHT11 ---
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO 4 (pin físico 7)

# --- Configuración de la matriz LED ---
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, rotate=0)

device.contrast(16)
device.clear()

font = ImageFont.load_default()

print("Mostrando temperatura en la matriz LED...")

while True:
    # Leer temperatura del DHT11
    humedad, temperatura = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    if temperatura is not None:
        mensaje = f" Temp: {temperatura}°C "
    else:
        mensaje = " Error al leer DHT11 "

    # Mostrar el mensaje desplazándose
    for i in range(len(mensaje) * 8):
        with canvas(device) as draw:
            draw.text((-i + device.width, -2), mensaje, fill="white", font=font)
        time.sleep(0.05)
