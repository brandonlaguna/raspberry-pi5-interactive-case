from RPLCD.i2c import CharLCD
import time

# Ajusta la dirección I²C según el escaneo
lcd = CharLCD('PCF8574', 0x27)  # 0x27 o 0x3F

lcd.clear()
lcd.write_string("Hola Raspberry Pi")
lcd.crlf()  # Salto de línea
lcd.write_string("LCD 16x2 I2C")

time.sleep(5)
lcd.clear()
