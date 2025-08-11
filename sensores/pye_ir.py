from gpiozero import MotionSensor
from RPLCD.i2c import CharLCD
import time

# PIR en GPIO 17
pir = MotionSensor(17)

# LCD en dirección I2C 0x27 (ajusta si es diferente)
lcd = CharLCD('PCF8574', 0x27)

lcd.clear()
lcd.write_string("Esperando...")

try:
    while True:
        pir.wait_for_motion()
        lcd.clear()
        lcd.write_string("Movimiento!")
        print("Movimiento detectado")
        time.sleep(2)
        lcd.clear()
        lcd.write_string("Esperando...")

except KeyboardInterrupt:
    lcd.clear()
    lcd.write_string("Adios")
