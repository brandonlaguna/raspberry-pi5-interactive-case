from RPLCD.i2c import CharLCD
from time import sleep

# Inicializa el LCD en la dirección I2C 0x27 (cambia si es necesario)
lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

try:
    # Mostrar mensaje en la primera línea
    lcd.write_string("Maleta Interactiva")
    sleep(2)
    
    # Borrar y escribir en dos líneas
    lcd.clear()
    lcd.write_string("Raspberry Pi 5")
    lcd.crlf()  # Salto a la segunda línea
    lcd.write_string("LCD 16x2 I2C")
    sleep(5)

    # Mensaje final con scroll simple
    lcd.clear()
    mensaje = "Proyecto de grado "
    for i in range(len(mensaje)):
        lcd.clear()
        lcd.write_string(mensaje[i:] + mensaje[:i])
        sleep(0.3)

finally:
    lcd.clear()
    lcd.close(clear=True)
