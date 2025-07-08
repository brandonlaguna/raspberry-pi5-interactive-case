import time
import keyboard
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas

# Configuraciones iniciales
block_orientations = [0, 90, 180, 270]
rotations = [0, 1, 2, 3]

bo_index = 0
rot_index = 0

def crear_dispositivo(bo, rot):
    serial = spi(port=0, device=0, gpio=noop())
    return max7219(serial, cascaded=4, block_orientation=bo, rotate=rot)

device = crear_dispositivo(block_orientations[bo_index], rotations[rot_index])

print("\nPresiona:")
print("  [o] para cambiar orientación")
print("  [r] para rotar")
print("  [q] para salir\n")

try:
    while True:
        with canvas(device) as draw:
            draw.text((0, 0), "Hola", fill="white")

        time.sleep(0.1)

        if keyboard.is_pressed('o'):
            bo_index = (bo_index + 1) % len(block_orientations)
            print(f"-> block_orientation = {block_orientations[bo_index]}")
            device = crear_dispositivo(block_orientations[bo_index], rotations[rot_index])
            time.sleep(0.3)

        if keyboard.is_pressed('r'):
            rot_index = (rot_index + 1) % len(rotations)
            print(f"-> rotate = {rotations[rot_index]}")
            device = crear_dispositivo(block_orientations[bo_index], rotations[rot_index])
            time.sleep(0.3)

        if keyboard.is_pressed('q'):
            print("\nSaliendo...")
            break

except KeyboardInterrupt:
    print("\nInterrumpido por el usuario.")

finally:
    device.clear()
