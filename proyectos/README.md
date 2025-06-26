# Proyecto: Estación de Monitoreo Ambiental con Raspberry Pi 5 y Flask

## Descripción del Proyecto

Este proyecto tiene como objetivo construir una estación de monitoreo ambiental utilizando una **Raspberry Pi 5**, varios sensores de medición y el framework web **Flask**. La aplicación web resultante mostrará los datos de los sensores en tiempo real, accesible desde cualquier dispositivo en la red local.

Este proyecto está diseñado para estudiantes interesados en el Internet de las Cosas (IoT), la programación en Python, la electrónica y el desarrollo web básico.

## Objetivos de Aprendizaje

- Familiarizarse con la Raspberry Pi 5 y su configuración.
- Conectar y leer datos de diferentes tipos de sensores electrónicos.
- Programar en Python para interactuar con hardware y el framework Flask.
- Desarrollar una aplicación web sencilla para visualizar datos.
- Entender los conceptos básicos de la comunicación I2C y SPI.
- Poner en práctica habilidades de resolución de problemas con hardware y software.

## Materiales Necesarios

Asegúrate de tener todos estos componentes antes de comenzar:

### Hardware

- **1x Raspberry Pi 5** (con fuente de alimentación USB-C y disipador/ventilador)
- **1x Tarjeta microSD** (16GB o más, Clase 10)
- **1x Lector de tarjetas microSD**
- **1x Sensor DHT11 o DHT22** (Temperatura y Humedad) - _Recomendado DHT22 por mayor precisión_
- **1x Sensor BMP180 o BME280** (Presión barométrica, Temperatura, Altitud - BME280 también mide humedad) - _Recomendado BME280 por versatilidad_
- **1x Sensor LDR** (Fotorresistencia para luminosidad)
- **1x Convertidor Analógico-Digital ADC MCP3008** (Necesario para el LDR)
- **1x Protoboard**
- **Cables jumper** (macho-hembra, macho-macho)
- **Resistencias** (10kΩ para el LDR)
- Monitor, teclado y ratón (para la configuración inicial o acceso directo)
- Cable HDMI (micro HDMI a HDMI estándar)
- Cable de red Ethernet (opcional) o adaptador WiFi

### Software

- **Raspberry Pi OS Lite** (recomendado para ahorrar recursos) o Raspberry Pi OS Desktop
- **Python 3**
- **Bibliotecas Python:** `RPi.GPIO`, `Adafruit_DHT`, `smbus`, `smbus2`, `Pillow`, `Adafruit_BME280` (o `Adafruit_BMP`), `spidev`
- **Flask**

## Estructura del Proyecto

├── app.py
├── sensor_readings.py
└── templates/
└── index.html

- `app.py`: El archivo principal de la aplicación Flask, maneja las rutas web y renderiza la página.
- `sensor_readings.py`: Módulo Python que contiene la lógica para leer los datos de los sensores.
- `templates/`: Carpeta que almacena los archivos HTML renderizados por Flask.
  - `index.html`: La plantilla HTML de la página web que muestra los datos de los sensores.

## 1. Configuración Inicial de la Raspberry Pi 5

### 1.1. Preparación de la Tarjeta microSD

1.  Descarga e instala **Raspberry Pi Imager** desde [https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/).
2.  Inserta tu tarjeta microSD.
3.  Abre Raspberry Pi Imager, selecciona `Raspberry Pi OS Lite (64-bit)` (o la versión de escritorio) y tu tarjeta.
4.  Haz clic en el icono de engranaje (Configuración Avanzada) y:
    - Habilita SSH.
    - Establece un usuario y contraseña.
    - Configura la Wi-Fi (si la usarás).
    - Configura la localización.
5.  Haz clic en "Write" y espera a que el proceso termine.

### 1.2. Primer Arranque y Actualización

1.  Inserta la tarjeta microSD en la Raspberry Pi 5.
2.  Conecta periféricos (monitor, teclado, ratón) y la fuente de alimentación.
3.  Una vez iniciado el sistema, abre una terminal y actualiza los paquetes:
    ```bash
    sudo apt update
    sudo apt upgrade -y
    ```

### 1.3. Habilitar Interfaces

Para la comunicación con los sensores, habilita I2C y SPI:

1.  Ejecuta:
    ```bash
    sudo raspi-config
    ```
2.  Navega a **3 Interface Options**.
3.  Selecciona **P3 I2C** y elige **Yes**.
4.  Selecciona **P4 SPI** y elige **Yes**.
5.  Sal de `raspi-config` y reinicia la Raspberry Pi.

## 2. Conexión de Sensores

**¡IMPORTANTE!** Asegúrate de que la Raspberry Pi esté **APAGADA y DESCONECTADA de la alimentación** antes de realizar cualquier conexión de hardware.

### 2.1. Pinout de la Raspberry Pi 5

Familiarízate con los pines GPIO de tu Raspberry Pi 5.

![Raspberry Pi 5 GPIO Pinout Diagram](images/pi5_gpio_pinout.png)
_(Esta imagen es un marcador de posición, deberías reemplazarla con una imagen real del pinout de la Pi 5 si es posible)._

### 2.2. Conexión del Sensor DHT11/DHT22

- **Pin VCC/3V3:** Raspberry Pi 3.3V (Pin 1 ó 17)
- **Pin GND:** Raspberry Pi GND (cualquier pin GND)
- **Pin Data:** Raspberry Pi GPIO 4 (Pin 7)

### 2.3. Conexión del Sensor BMP180/BME280 (I2C)

- **Pin VCC/3V3:** Raspberry Pi 3.3V (Pin 1 ó 17)
- **Pin GND:** Raspberry Pi GND
- **Pin SDA:** Raspberry Pi GPIO 2 (Pin 3)
- **Pin SCL:** Raspberry Pi GPIO 3 (Pin 5)

### 2.4. Conexión del Sensor LDR con MCP3008 (ADC)

| Pin MCP3008 | Conexión Raspberry Pi   |
| :---------- | :---------------------- |
| VDD         | 3.3V (Pin 1 ó 17)       |
| VREF        | 3.3V (Pin 1 ó 17)       |
| AGND        | GND                     |
| CLK         | SCLK (GPIO 11 - Pin 23) |
| DOUT        | MISO (GPIO 9 - Pin 21)  |
| DIN         | MOSI (GPIO 10 - Pin 19) |
| CS/SHDN     | CE0 (GPIO 8 - Pin 24)   |
| DGND        | GND                     |

**LDR al MCP3008:**

1.  Un extremo del LDR a 3.3V.
2.  El otro extremo del LDR a **MCP3008 CH0** (Pin 13).
3.  Una resistencia de 10kΩ desde **MCP3008 CH0** a GND.

## 3. Instalación de Bibliotecas Python

1.  **Actualizar pip:**
    ```bash
    sudo apt install python3-pip -y
    pip install --upgrade pip
    ```
2.  **Instalar Bibliotecas para DHT11/DHT22:**
    ```bash
    sudo pip3 install Adafruit_DHT
    ```
3.  **Instalar Bibliotecas para I2C (BMP180/BME280):**
    ```bash
    sudo apt install i2c-tools -y
    sudo pip3 install smbus smbus2
    sudo pip3 install adafruit-circuitpython-bme280 # O adafruit-circuitpython-bmp280
    ```
    Verifica el sensor con: `i2cdetect -y 1`
4.  **Instalar Bibliotecas para SPI (MCP3008):**
    ```bash
    sudo pip3 install spidev
    ```
5.  **Instalar Flask:**
    ```bash
    pip3 install Flask
    ```

## 4. Ejecución de la Aplicación Flask

Para poner en marcha tu aplicación web Flask y ver los datos de los sensores en acción, sigue estos pasos:

1.  **Abre una terminal en tu Raspberry Pi.** Puedes hacerlo directamente desde el entorno de escritorio de la Raspberry Pi, o a través de SSH desde otra computadora.

2.  **Navega a la carpeta de tu proyecto.** Asegúrate de estar en el directorio donde guardaste los archivos `app.py` y `sensor_readings.py`, y la carpeta `templates/`.

    ```bash
    cd my_sensor_app/
    ```

3.  **Ejecuta la aplicación Flask:**

    ```bash
    python3 app.py
    ```

4.  **Verás una salida similar a esta:**

    ```
     * Serving Flask app 'app'
     * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on [http://0.0.0.0:5000](http://0.0.0.0:5000)
    Press CTRL+C to quit
    ```

    La línea `* Running on http://0.0.0.0:5000` te indica que el servidor web Flask está escuchando en todas las interfaces de red de tu Raspberry Pi en el puerto `5000`. Esto significa que la aplicación será accesible desde cualquier dispositivo conectado a la misma red local que tu Raspberry Pi.

5.  **Para acceder a la página web:**

    - **Si estás usando el navegador web de la propia Raspberry Pi**, abre:

      - `http://localhost:5000`
      - o `http://127.0.0.1:5000`

    - **Si estás en otra computadora o dispositivo (como un teléfono o laptop) en la misma red local**, necesitarás la dirección IP de tu Raspberry Pi. Puedes encontrarla ejecutando el siguiente comando en la terminal de tu Raspberry Pi:

      ```bash
      hostname -I
      ```

      Por ejemplo, si el comando te devuelve `192.168.1.100`, entonces abre `http://192.168.1.100:5000` en el navegador de tu computadora.
