import RPi.GPIO as GPIO
import time

# Configurar pines
TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def medir_distancia():
    # Enviar pulso
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Esperar respuesta
    while GPIO.input(ECHO) == 0:
        inicio = time.time()
    while GPIO.input(ECHO) == 1:
        fin = time.time()

    duracion = fin - inicio
    distancia = (duracion * 34300) / 2  # velocidad del sonido 34300 cm/s
    return distancia

try:
    print("Midiendo distancia. Ctrl+C para salir.")
    while True:
        distancia = medir_distancia()
        print(f"Distancia: {distancia:.2f} cm")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMedición detenida.")
finally:
    GPIO.cleanup()
