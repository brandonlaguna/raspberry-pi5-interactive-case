from pad4pi import rpi_gpio
from RPLCD.i2c import CharLCD
import time

# ===== CONFIGURACIÓN DEL LCD I²C =====
lcd = CharLCD(
    i2c_expander='PCF8574',
    address=0x27,  # Dirección I²C (puede variar, usar i2cdetect para confirmar)
    port=1,
    cols=16,
    rows=2,
    charmap='A02'
)

# ===== CONFIGURACIÓN DEL TECLADO 3x4 =====
KEYPAD = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"]
]

ROW_PINS = [5, 6, 13, 19]  # Filas
COL_PINS = [12, 16, 20]    # Columnas

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

# ===== CONFIGURACIÓN DE CONTRASEÑA =====
PASSWORD = "1234"
input_code = ""

# ===== FUNCIÓN DE TECLA PRESIONADA =====
def key_pressed(key):
    global input_code

    if key == "#":  # Confirmar entrada
        lcd.clear()
        if input_code == PASSWORD:
            lcd.write_string("Clave correcta")
        else:
            lcd.write_string("Clave incorrecta")
        time.sleep(2)
        lcd.clear()
        input_code = ""  # Reset para siguiente intento

    elif key == "*":  # Borrar entrada
        input_code = ""
        lcd.clear()
        lcd.write_string("Clave borrada")

    else:
        input_code += key
        lcd.clear()
        lcd.write_string("*" * len(input_code))  # Mostrar asteriscos

# ===== REGISTRAR FUNCIÓN EN EL TECLADO =====
keypad.registerKeyPressHandler(key_pressed)

# ===== LOOP PRINCIPAL =====
lcd.clear()
lcd.write_string("Ingrese clave:")

try:
    while True:
        time.sleep(0.2)

except KeyboardInterrupt:
    keypad.cleanup()
    lcd.clear()
