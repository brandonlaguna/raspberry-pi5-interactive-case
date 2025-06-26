import spidev
import time

# Inicializar SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, CS 0
spi.max_speed_hz = 1350000

def leer_canal(ch):
    adc = spi.xfer2([1, (8 + ch) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    print("Midiendo nivel de luz (LDR). Ctrl+C para salir.")
    while True:
        luz = leer_canal(0)  # canal 0 del MCP3008
        print(f"Luz (valor analógico): {luz}")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nLectura detenida.")
finally:
    spi.close()
