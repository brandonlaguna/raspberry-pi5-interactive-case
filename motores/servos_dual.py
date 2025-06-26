import RPi.GPIO as GPIO
import time

# Pines GPIO usados para los servos
servo_1_pin = 17  # Conecta el primer servo a GPIO 17 (pin físico 11)
servo_2_pin = 27  # Conecta el segundo servo a GPIO 27 (pin físico 13)

# Configurar el modo de numeración de pines
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_1_pin, GPIO.OUT)
GPIO.setup(servo_2_pin, GPIO.OUT)

# Crear señales PWM a 50Hz (frecuencia típica para servos)
servo1 = GPIO.PWM(servo_1_pin, 50)
servo2 = GPIO.PWM(servo_2_pin, 50)

# Iniciar PWM con duty cycle 0
servo1.start(0)
servo2.start(0)

# Función para mover un servo a cierto ángulo (entre 0° y 180°)
def set_angle(servo, angle):
    duty = 2 + (angle / 18)  # Fórmula para convertir ángulo a duty cycle
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo.ChangeDutyCycle(0)  # Detiene la señal para evitar zumbido

try:
    print("Moviendo servos a 0°, 90°, 180°...")

    # Primer servo
    set_angle(servo1, 0)
    time.sleep(1)
    set_angle(servo1, 90)
    time.sleep(1)
    set_angle(servo1, 180)
    time.sleep(1)

    # Segundo servo
    set_angle(servo2, 0)
    time.sleep(1)
    set_angle(servo2, 90)
    time.sleep(1)
    set_angle(servo2, 180)
    time.sleep(1)

except KeyboardInterrupt:
    print("\nEjecución interrumpida por el usuario.")

finally:
    # Detener PWM y liberar pines
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()
