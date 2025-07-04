from flask import Flask, request, render_template_string
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.virtual import viewport
from luma.core.render import canvas
from PIL import ImageFont
import threading
import time

app = Flask(__name__)

# Configura el SPI y la pantalla LED
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=90, rotate=0)
device.contrast(10)

# Fuente
font = ImageFont.load_default()

# Mensaje actual
current_message = "¡Hola desde Flask y Raspberry Pi!   "

# Scroll settings
scroll_speed = 0.05  # segundos entre cada desplazamiento

# Función para desplazar el texto
def scroll_text():
    global current_message
    while True:
        text_width = font.getsize(current_message)[0]
        virtual = viewport(device, width=text_width + device.width, height=8)

        with canvas(virtual) as draw:
            draw.text((0, 0), current_message, fill="white", font=font)

        for x in range(text_width + device.width):
            virtual.set_position((x, 0))
            time.sleep(scroll_speed)

# Iniciar el scroll en un hilo aparte
threading.Thread(target=scroll_text, daemon=True).start()

# Página web básica
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>Mensaje LED</title></head>
<body>
  <h2>Enviar mensaje al panel LED</h2>
  <form action="/" method="POST">
    <input type="text" name="message" maxlength="100" required>
    <input type="submit" value="Mostrar">
  </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    global current_message
    if request.method == 'POST':
        # Agregamos espacios para que el texto se separe entre ciclos
        current_message = request.form['message'] + "   "
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)