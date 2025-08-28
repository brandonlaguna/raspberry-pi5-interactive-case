# 🚦 Semáforo con módulo Keyestudio

Este documento describe el funcionamiento y las conexiones del **módulo de semáforo Keyestudio** controlado desde la **Raspberry Pi 5** usando la librería `lgpio`.

La carpeta contiene un único archivo de ejemplo (`semaforo.py`) que simula el ciclo de un semáforo vehicular (verde → amarillo → rojo) con temporización.

---

## 📂 Archivos incluidos

| Archivo       | Descripción                                           |
| ------------- | ----------------------------------------------------- |
| `semaforo.py` | Script que controla el módulo semáforo vía GPIO       |
| `README.md`   | Este archivo, con la documentación del uso            |

---

## 🔧 Requisitos de hardware

| Componente                  | Detalles                                           |
| --------------------------- | -------------------------------------------------- |
| Raspberry Pi 5              | GPIO habilitado, sistema con Python 3 instalado    |
| Módulo semáforo Keyestudio  | Incluye LEDs Rojo, Amarillo y Verde                |
| Resistencias (si aplica)    | Generalmente ya vienen integradas en el módulo     |
| Cables jumper               | Para conexión de GPIOs                             |

---

## 1. ⚙️ Configuración del ambiente de desarrollo

Se recomienda crear un **ambiente virtual** para mantener las dependencias separadas del sistema principal de Raspberry Pi OS.

- Ubícate en la carpeta del proyecto:

```bash
cd ~/Documents/raspberry-pi5-interactive-case/semaforo
```

- Crear el ambiente virtual:

```bash
python3 -m venv env
```

- Activar el ambiente:

```bash
source env/bin/activate
```

> Al activarse, verás `(env)` al inicio de la línea de tu terminal, lo que indica que estás dentro del entorno virtual.

---

## 2. 📦 Instalación de dependencias

El script utiliza la librería `lgpio`, incluida en **Raspberry Pi OS** por defecto en la mayoría de distribuciones recientes.  
Si no está instalada, se puede instalar con:

```bash
sudo apt update
sudo apt install python3-lgpio
```

---

## 3. ⚡ Conexiones del módulo semáforo

Conecta los pines del **módulo Keyestudio** a la Raspberry Pi 5 según la siguiente tabla:

| LED       | GPIO en Raspberry Pi | Pin físico |
| --------- | -------------------- | ----------- |
| Rojo      | GPIO 17              | 11          |
| Amarillo  | GPIO 27              | 13          |
| Verde     | GPIO 22              | 15          |
| VCC       | 3.3V o 5V            | 1 o 2       |
| GND       | GND                  | 6           |

📌 **Nota:** Este módulo ya incluye resistencias, por lo que se puede conectar directamente a los GPIOs.

---

## 4. ▶️ Ejecución del script

Estando dentro del ambiente virtual y en la carpeta del proyecto:

```bash
python3 semaforo.py
```

El ciclo será el siguiente:

1. LED verde encendido por **5 segundos**.  
2. LED amarillo encendido por **2 segundos**.  
3. LED rojo encendido por **5 segundos**.  
4. El ciclo se repite indefinidamente.

Para detenerlo, presiona `CTRL + C`.  
El script apagará todos los LEDs antes de salir.

---

## 5. 📸 Ejemplo de uso

Cuando el script se ejecute correctamente, el **módulo semáforo Keyestudio** se comportará como un semáforo real, alternando entre verde, amarillo y rojo con la temporización definida en el código.

![Módulo semáforo Keyestudio](assets/semaforo_keystudio.png)

---

Con esta configuración podrás integrar un **sistema de semáforo básico** en tu maleta interactiva con Raspberry Pi 5 🚦.
