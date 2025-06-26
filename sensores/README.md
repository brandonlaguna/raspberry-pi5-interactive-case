# Sensores Básicos 🧪

Este directorio incluye el código y documentación para la conexión y lectura de **sensores básicos** con la **Raspberry Pi 5**. Los módulos cubiertos permiten medir temperatura, humedad, distancia, entre otros, y son ideales para aprender conceptos de electrónica y programación con Python.

---

## 📂 Estructura del directorio

- `dht11.py` – Sensor de **temperatura y humedad**.
- `hc_sr04.py` – Sensor ultrasónico de **distancia**.
- `ldr.py` – Sensor de luz **fotocélula**.
- `README.md` – Este archivo, que explica cómo usar los ejemplos y la filosofía detrás del diseño.

---

# 📦 Requisitos del Proyecto – Sensores Básicos

Este proyecto utiliza una **Raspberry Pi 5** para interactuar con sensores comunes como el **DHT11**, **HC-SR04** y **LDR** mediante Python. A continuación se detallan los requisitos de hardware, conexiones y software necesarios para su ejecución.

---

## 🧰 Hardware requerido

| Componente           | Descripción                                   |
| -------------------- | --------------------------------------------- |
| Raspberry Pi 5       | Con Raspberry Pi OS actualizado               |
| Sensor DHT11         | Sensor de temperatura y humedad digital       |
| Sensor HC-SR04       | Sensor ultrasónico de distancia               |
| Sensor LDR + MCP3008 | Sensor de luz con conversor analógico-digital |
| Protoboard           | Para montar los circuitos                     |
| Jumpers macho–macho  | Para conexiones entre GPIO y sensores         |
| Resistencias básicas | Para divisor de voltaje (LDR) o pull-up       |

---

## 🧪 Conexiones recomendadas

### 📌 DHT11

- DATA → GPIO 4
- VCC → 3.3V
- GND → GND

### 📌 HC-SR04

- TRIG → GPIO 23
- ECHO → GPIO 24 (usa divisor de voltaje para protección)
- VCC → 5V
- GND → GND

### 📌 LDR (con MCP3008)

- LDR conectada con resistencia en divisor de voltaje
- Señal → canal 0 del MCP3008 (CH0)
- MCP3008 SPI:
  - CLK → GPIO 11
  - MISO → GPIO 9
  - MOSI → GPIO 10
  - CS → GPIO 8

---

## 💻 Software y bibliotecas necesarias

Asegúrate de tener Python 3 instalado y ejecuta los siguientes comandos en tu Raspberry Pi:

```bash
sudo apt update
sudo apt install python3-pip python3-rpi.gpio python3-spidev
pip install adafruit-circuitpython-dht
```
