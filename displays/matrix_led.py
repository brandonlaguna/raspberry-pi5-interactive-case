from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from PIL import ImageFont, ImageDraw
import time

# Configuración del dispositivo
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=90, rotate=0)

# Tamaño total: 32x8 (4 matrices 8x8)
device.contrast(16)
device.clear()

# Fuente predeterminada
font = ImageFont.load_default()

# Mensaje a mostrar
mensaje = " Raspberry Pi 5 "

print("Mostrando mensaje en la matriz LED...")
while True:
    for i in range(len(mensaje) * 8):
        with canvas(device) as draw:
            draw.text((-i + device.width, 0), mensaje, fill="white", font=font)
        time.sleep(0.05)