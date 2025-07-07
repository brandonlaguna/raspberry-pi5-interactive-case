import lgpio
import time

SERVO_PIN = 18  # GPIO 18 (PWM0)
CHIP = 0

h = lgpio.gpiochip_open(CHIP)

try:
    # Configurar señal PWM de 50Hz
    lgpio.tx_pwm(h, SERVO_PIN, 50, 7.5)  # 7.5% = posición media
    time.sleep(2)

    # Girar a 0°
    lgpio.tx_pwm(h, SERVO_PIN, 50, 2.5)
    print("0 grados")
    time.sleep(2)

    # Girar a 90°
    lgpio.tx_pwm(h, SERVO_PIN, 50, 7.5)
    print("90 grados")
    time.sleep(2)

    # Girar a 180°
    lgpio.tx_pwm(h, SERVO_PIN, 50, 12.5)
    print("180 grados")
    time.sleep(2)

    # Volver al centro
    lgpio.tx_pwm(h, SERVO_PIN, 50, 7.5)
    time.sleep(1)

finally:
    lgpio.tx_pwm(h, SERVO_PIN, 0, 0)
    lgpio.gpiochip_close(h)
