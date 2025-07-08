import lgpio
import time

# GPIOs para LEDs
ROJO = 17
AMARILLO = 27
VERDE = 22

# Abrir controlador
h = lgpio.gpiochip_open(0)

# Configurar pines como salida
lgpio.gpio_claim_output(h, ROJO)
lgpio.gpio_claim_output(h, AMARILLO)
lgpio.gpio_claim_output(h, VERDE)

try:
    while True:
        # Verde
        lgpio.gpio_write(h, VERDE, 1)
        lgpio.gpio_write(h, AMARILLO, 0)
        lgpio.gpio_write(h, ROJO, 0)
        time.sleep(5)

        # Amarillo
        lgpio.gpio_write(h, VERDE, 0)
        lgpio.gpio_write(h, AMARILLO, 1)
        time.sleep(2)

        # Rojo
        lgpio.gpio_write(h, AMARILLO, 0)
        lgpio.gpio_write(h, ROJO, 1)
        time.sleep(5)

except KeyboardInterrupt:
    print("Detenido por el usuario")

finally:
    lgpio.gpio_write(h, ROJO, 0)
    lgpio.gpio_write(h, AMARILLO, 0)
    lgpio.gpio_write(h, VERDE, 0)
    lgpio.gpiochip_close(h)
