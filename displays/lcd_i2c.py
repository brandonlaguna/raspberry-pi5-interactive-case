import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD

# Configuración GPIO
PIR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# Configuración LCD (dirección I2C 0x27 o 0x3F según tu módulo)
lcd = CharLCD('PCF8574', 0x27)

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Movimiento detectado")
            lcd.clear()
            lcd.write_string("Movimiento")
            lcd.cursor_pos = (1, 0)
            lcd.write_string("detectado!")
        else:
            print("Sin movimiento")
            lcd.clear()
            lcd.write_string("Sin movimiento")
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
