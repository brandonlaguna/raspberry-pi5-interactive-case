# sensor_readings.py

import Adafruit_DHT
import board
import busio
import adafruit_bme280 # O adafruit_bmp280 si usas BMP180
import spidev
import time
import RPi.GPIO as GPIO # No es estrictamente necesario para los sensores aquí, pero útil para GPIO en general

# Configuración del sensor DHT11/DHT22
DHT_SENSOR = Adafruit_DHT.DHT22  # O Adafruit_DHT.DHT11
DHT_PIN = 4                      # GPIO4 (Pin 7 en la Raspberry Pi)

# Configuración del sensor BME280/BMP180 (I2C)
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76) # O 0x77, verifica con i2cdetect -y 1

# Ajuste de altitud para el BME280 (opcional, para una lectura de presión más precisa)
# bme280.sea_level_pressure = 1013.25 # Presión a nivel del mar promedio en hPa (hectopascales)

# Configuración del MCP3008 (SPI)
spi = spidev.SpiDev()
spi.open(0, 0) # Abrir bus SPI 0, dispositivo 0 (CE0)
spi.max_speed_hz = 1000000 # Velocidad máxima de comunicación SPI

# Función para leer el ADC (MCP3008)
def read_adc(channel):
    # Asegurarse de que el canal está en el rango válido (0-7)
    if not 0 <= channel <= 7:
        raise ValueError('Canal ADC inválido. Debe ser de 0 a 7.')

    # El MCP3008 necesita un byte de inicio (1), un bit de modo (single-ended = 1, differential = 0),
    # y los 3 bits del número de canal.
    # El bit de modo single-ended siempre es 1.
    # Los 3 bits del canal se codifican como (channel << 4).
    # Finalmente, se leen 2 bytes.
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    # Los 10 bits de datos están en los últimos 2 bytes de la respuesta.
    # El primer byte tiene los 2 bits más significativos y el segundo byte tiene los 8 bits menos significativos.
    adc_out = ((r[1] & 3) << 8) + r[2]
    return adc_out

# Función para obtener todos los datos de los sensores
def get_sensor_data():
    data = {}

    # Leer DHT11/DHT22
    humidity, temperature_dht = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature_dht is not None:
        data['temperature_dht'] = round(temperature_dht, 2)
        data['humidity_dht'] = round(humidity, 2)
    else:
        data['temperature_dht'] = "Error"
        data['humidity_dht'] = "Error"

    # Leer BME280/BMP180
    try:
        data['temperature_bme'] = round(bme280.temperature, 2)
        data['pressure_bme'] = round(bme280.pressure, 2)
        data['altitude_bme'] = round(bme280.altitude, 2)
        if hasattr(bme280, 'humidity'): # BME280 tiene humedad, BMP180 no
            data['humidity_bme'] = round(bme280.humidity, 2)
        else:
            data['humidity_bme'] = "N/A" # No aplica para BMP180
    except Exception as e:
        print(f"Error al leer BME280/BMP180: {e}")
        data['temperature_bme'] = "Error"
        data['pressure_bme'] = "Error"
        data['altitude_bme'] = "Error"
        data['humidity_bme'] = "Error"

    # Leer LDR (MCP3008, canal 0)
    try:
        ldr_value = read_adc(0) # Asumiendo LDR conectado al canal 0 del MCP3008
        # Convertir el valor ADC (0-1023) a un porcentaje de luminosidad o valor representativo
        # Un valor más alto significa menos luz (mayor resistencia del LDR)
        # Un valor más bajo significa más luz (menor resistencia del LDR)
        data['luminosity'] = round((1023 - ldr_value) / 10.23, 2) # Porcentaje de luminosidad (aproximado)
        data['ldr_raw'] = ldr_value
    except Exception as e:
        print(f"Error al leer LDR: {e}")
        data['luminosity'] = "Error"
        data['ldr_raw'] = "Error"

    return data

if __name__ == '__main__':
    # Ejemplo de uso:
    try:
        while True:
            data = get_sensor_data()
            print("\n--- Datos de Sensores ---")
            print(f"Temperatura (DHT): {data['temperature_dht']} °C")
            print(f"Humedad (DHT): {data['humidity_dht']} %")
            print(f"Temperatura (BME/BMP): {data['temperature_bme']} °C")
            print(f"Presión (BME/BMP): {data['pressure_bme']} hPa")
            print(f"Altitud (BME/BMP): {data['altitude_bme']} m")
            print(f"Humedad (BME): {data['humidity_bme']} %")
            print(f"Luminosidad: {data['luminosity']} %")
            print(f"LDR Raw: {data['ldr_raw']}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Lectura de sensores detenida.")
    finally:
        spi.close() # Cerrar la conexión SPI al salir