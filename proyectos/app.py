# app.py

from flask import Flask, render_template, jsonify
import sensor_readings
import time

app = Flask(__name__)

@app.route('/')
def index():
    """Ruta principal que renderiza la página HTML."""
    return render_template('index.html')

@app.route('/data')
def get_data():
    """Ruta API que devuelve los datos de los sensores en formato JSON."""
    data = sensor_readings.get_sensor_data()
    # Añadir un timestamp para saber cuándo se tomaron los datos
    data['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(data)

if __name__ == '__main__':
    # Ejecutar la aplicación Flask
    # host='0.0.0.0' hace que la aplicación sea accesible desde cualquier IP en la red local
    # debug=True es útil para el desarrollo, pero debe ser False en producción
    app.run(host='0.0.0.0', port=5000, debug=True)