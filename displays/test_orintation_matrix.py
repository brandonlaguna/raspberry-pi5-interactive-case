import time
import curses
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas

# Lista de opciones
block_orientations = [0, 90, 180, 270]
rotations = [0, 1, 2, 3]

# Índices actuales
bo_index = 0
rot_index = 0

def crear_dispositivo(bo, rot):
    serial = spi(port=0, device=0, gpio=noop())
    return max7219(serial, cascaded=4, block_orientation=bo, rotate=rot)

def main(stdscr):
    global bo_index, rot_index

    stdscr.nodelay(True)  # No bloquea en getch()
    stdscr.clear()
    stdscr.addstr(0, 0, "Presiona O = orientación, R = rotar, Q = salir")

    device = crear_dispositivo(block_orientations[bo_index], rotations[rot_index])

    try:
        while True:
            with canvas(device) as draw:
                draw.text((0, 0), "Hola", fill="white")

            key = stdscr.getch()

            if key == ord('o') or key == ord('O'):
                bo_index = (bo_index + 1) % len(block_orientations)
                device = crear_dispositivo(block_orientations[bo_index], rotations[rot_index])
                stdscr.addstr(2, 0, f"block_orientation = {block_orientations[bo_index]}   ")
            elif key == ord('r') or key == ord('R'):
                rot_index = (rot_index + 1) % len(rotations)
                device = crear_dispositivo(block_orientations[bo_index], rotations[rot_index])
                stdscr.addstr(3, 0, f"rotate = {rotations[rot_index]}   ")
            elif key == ord('q') or key == ord('Q'):
                break

            time.sleep(0.1)

    finally:
        device.clear()

# Ejecutar curses
curses.wrapper(main)
