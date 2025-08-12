import lgpio
import time
from RPLCD.i2c import CharLCD

# ----------------------------
# CONFIG LCD I2C
# ----------------------------
I2C_ADDR = 0x27  # Dirección del módulo I2C del LCD
lcd = CharLCD('PCF8574', I2C_ADDR, port=1, cols=16, rows=2)

# ----------------------------
# CONFIG TECLADO 3x4
# ----------------------------
KEYPAD = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"]
]

# Pines BCM
ROW_PINS = [17, 27, 22, 5]  # Filas
COL_PINS = [6, 13, 19]      # Columnas
RELAY_PIN = 21              # Pin de control del relé

# Contraseña
PASSWORD = "1235"
input_buffer = ""

# Estado del relé (True = cerrado, False = abierto)
relay_state = True  # Arranca cerrado

# ----------------------------
# INICIALIZAR GPIO con lgpio
# ----------------------------
h = lgpio.gpiochip_open(0)

# Filas como salidas (apagadas inicialmente)
for r in ROW_PINS:
    lgpio.gpio_claim_output(h, r)
    lgpio.gpio_write(h, r, 1)

# Columnas como entradas con pull-up
for c in COL_PINS:
    lgpio.gpio_claim_input(h, c, lgpio.SET_PULL_UP)

# Relé como salida
lgpio.gpio_claim_output(h, RELAY_PIN)
lgpio.gpio_write(h, RELAY_PIN, 1 if relay_state else 0)  # Cerrar relé al inicio

# ----------------------------
# FUNCIONES
# ----------------------------
def scan_keypad():
    """Escanea el teclado y devuelve la tecla presionada o None."""
    for i, row in enumerate(ROW_PINS):
        lgpio.gpio_write(h, row, 0)
        for j, col in enumerate(COL_PINS):
            if lgpio.gpio_read(h, col) == 0:
                time.sleep(0.02)  # antirrebote
                while lgpio.gpio_read(h, col) == 0:
                    pass
                lgpio.gpio_write(h, row, 1)
                return KEYPAD[i][j]
        lgpio.gpio_write(h, row, 1)
    return None

def toggle_relay():
    """Invierte el estado del relé."""
    global relay_state
    relay_state = not relay_state
    lgpio.gpio_write(h, RELAY_PIN, 1 if relay_state else 0)

def process_key(key):
    global input_buffer
    if key == "#":  # Confirmar
        lcd.clear()
        if input_buffer == PASSWORD:
            lcd.write_string("Correcto!")
            toggle_relay()
        else:
            lcd.write_string("Incorrecto!")
        time.sleep(2)
        lcd.clear()
        lcd.write_string("Ingrese clave:")
        input_buffer = ""
    elif key == "*":  # Borrar
        input_buffer = ""
        lcd.clear()
        lcd.write_string("Ingrese clave:")
    else:
        input_buffer += key
        lcd.clear()
        lcd.write_string("*" * len(input_buffer))

# ----------------------------
# LOOP PRINCIPAL
# ----------------------------
try:
    lcd.clear()
    lcd.write_string("Ingrese clave:")
    while True:
        k = scan_keypad()
        if k:
            process_key(k)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nSaliendo...")
finally:
    lgpio.gpiochip_close(h)
    lcd.clear()
