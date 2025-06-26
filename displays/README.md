# 📺 Displays y Visualización de Datos

Esta carpeta contiene ejemplos prácticos para la conexión y uso de **displays en Raspberry Pi 5**, permitiendo mostrar datos obtenidos desde sensores o scripts personalizados.

Los módulos utilizados se conectan por **I2C o SPI** y permiten visualizar texto, símbolos o mensajes en tiempo real.

---

## 📂 Archivos incluidos

| Archivo         | Descripción                                           |
| --------------- | ----------------------------------------------------- |
| `lcd_i2c.py`    | Muestra texto en una pantalla LCD 16x2 I2C            |
| `matrix_led.py` | Muestra texto desplazable en módulo LED 8x8 (MAX7219) |
| `README.md`     | Este archivo, con la documentación del uso            |

---

## 🔧 Requisitos de hardware

| Componente                  | Detalles                          |
| --------------------------- | --------------------------------- |
| Raspberry Pi 5              | GPIO habilitado, I2C/SPI activos  |
| Pantalla LCD 16x2 + I2C     | Módulo con dirección común `0x27` |
| Módulo LED 8x8 x4 (MAX7219) | Conexión SPI estándar             |
| Cables jumper               | Para conexión de los displays     |

---

## 📦 Instalación de dependencias

Instala las bibliotecas necesarias para los dos tipos de pantallas:

```bash
sudo apt update
sudo apt install python3-pip i2c-tools
pip3 install RPLCD luma.led_matrix luma.core

# Conexiones de Displays para Raspberry Pi 5

Este documento detalla las conexiones recomendadas para el funcionamiento de dos tipos de displays:

1. **LCD 16x2 con módulo I2C**
2. **Módulo de 4 matrices LED 8x8 (MAX7219) vía SPI**

---

## 1. LCD 16x2 (I2C)

Conecta el display LCD con el adaptador I2C de la siguiente forma:

| Señal | Conexión en Raspberry Pi |
|-------|--------------------------|
| SDA   | GPIO 2 (Pin 3)           |
| SCL   | GPIO 3 (Pin 5)           |
| VCC   | 5V                       |
| GND   | GND                      |

> **Nota:** Puedes utilizar el comando `sudo i2cdetect -y 1` para verificar la dirección I2C (generalmente `0x27`).

---

## 2. Módulo de 4 matrices LED 8x8 (MAX7219) – SPI

Para el módulo MAX7219, se recomienda conectar según la siguiente tabla:

| Señal | Conexión en Raspberry Pi |
|-------|--------------------------|
| DIN (Data In) | GPIO 10 (MOSI)    |
| CS            | GPIO 8 (CE0)      |
| CLK           | GPIO 11 (SCLK)    |
| VCC           | 5V                |
| GND           | GND               |

> **Importante:**
> - Asegúrate de habilitar el modo SPI en tu Raspberry Pi.
> - El módulo se comunica vía SPI, por lo que es necesario que la interfaz esté activa.
>   Para ello, puedes activarla desde `sudo raspi-config → Interfacing Options → SPI → Enable`.

---

Con estas conexiones, podrás integrar ambos displays en tu proyecto basado en Raspberry Pi 5. Si necesitas ajustar direcciones o pines según tu esquema específico, revisa la documentación del módulo o del adaptador utilizado.
```
