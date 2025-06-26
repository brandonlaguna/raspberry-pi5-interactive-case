# Sensores Básicos 🧪

Este directorio incluye el código y documentación para la conexión y lectura de **sensores básicos** con la **Raspberry Pi 5**. Los módulos cubiertos permiten medir temperatura, humedad, distancia, entre otros, y son ideales para aprender conceptos de electrónica y programación con Python.

---

## 📂 Estructura del directorio

- `dht11.py` – Sensor de **temperatura y humedad**.
- `hc_sr04.py` – Sensor ultrasónico de **distancia**.
- `ldr.py` – Sensor de luz **fotocélula**.
- `README.md` – Este archivo, que explica cómo usar los ejemplos y la filosofía detrás del diseño.

---

## 🔧 Requisitos

- Raspberry Pi 5 con Raspberry Pi OS actualizado.
- Python 3 instalado.
- Bibliotecas necesarias:
  ```bash
  pip install RPi.GPIO adafruit-circuitpython-dht
  sudo apt install python3-rpi.gpio
  ```
