import time
import board
import adafruit_dht

# Inicializar el sensor DHT11 en el pin GPIO 4
dhtDevice = adafruit_dht.DHT11(board.D4)

print("Leyendo datos del DHT11. Presiona Ctrl+C para detener.")

try:
    while True:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity

        if temperature_c is not None and humidity is not None:
            print(f"Temperatura: {temperature_c:.1f} °C  |  Humedad: {humidity:.1f} %")
        else:
            print("Fallo en la lectura del sensor.")

        time.sleep(2)

except KeyboardInterrupt:
    print("\nLectura finalizada.")
except Exception as e:
    print(f"Error: {e}")
finally:
    dhtDevice.exit()
