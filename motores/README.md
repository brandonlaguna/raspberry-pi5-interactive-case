# ⚙️ Control de Servomotores con Raspberry Pi 5

Esta carpeta contiene un ejemplo funcional para controlar **dos servomotores SG90** utilizando la Raspberry Pi 5 mediante señales PWM por GPIO. Los servos pueden utilizarse para mover objetos, apuntar sensores, abrir compuertas, entre otras aplicaciones mecánicas.

---

## 📂 Archivos incluidos

| Archivo          | Descripción                                           |
| ---------------- | ----------------------------------------------------- |
| `servos_dual.py` | Controla 2 servomotores desde GPIO                    |
| `README.md`      | Este archivo, con las instrucciones de conexión y uso |

---

## 🧰 Componentes necesarios

| Elemento                                     | Descripción                               |
| -------------------------------------------- | ----------------------------------------- |
| Raspberry Pi 5                               | Sistema de control con GPIO               |
| 2 × Servomotor SG90                          | Servos de 180° de rotación                |
| Fuente de alimentación externa (recomendado) | Para evitar sobrecarga en la Raspberry Pi |
| Cables jumper (macho-macho)                  | Para las conexiones físicas               |
| Protoboard (opcional)                        | Para montaje y distribución de voltaje    |

---

## 🔌 Conexiones

| Servomotor | Cable         | Conexión en Raspberry Pi          |
| ---------- | ------------- | --------------------------------- |
| Servo 1    | Marrón (GND)  | GND (Pin 6, 9 o 14)               |
|            | Rojo (VCC)    | 5V (Pin 2 o 4) o fuente externa\* |
|            | Naranja (PWM) | GPIO 17 (Pin 11)                  |
| Servo 2    | Marrón (GND)  | GND compartido                    |
|            | Rojo (VCC)    | 5V (Pin 2 o 4) o fuente externa\* |
|            | Naranja (PWM) | GPIO 27 (Pin 13)                  |

> ⚠️ _Si usas una fuente externa, asegúrate de unir las GND (Raspberry + fuente + servos)_.

---

## 💻 Instalación de dependencias

```bash
sudo apt update
sudo apt install python3-rpi.gpio
```
