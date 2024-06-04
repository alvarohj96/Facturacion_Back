from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

from imputacion_trabajador import ImputacionTrabajador
from trabajador import Trabajador
import dateutil.parser
import pytz

app = Flask(__name__)
CORS(app)  # Esto permitirá todas las solicitudes de todos los orígenes

trabajadores = [
    Trabajador("Juan Perez"),
    Trabajador("Laura Garcia"),
    Trabajador("Elena Torres"),
    Trabajador("Carlos Sanchez")
]

@app.route('/log', methods=['POST'])
def log_message():
    if request.is_json:
        data = request.get_json()
        fecha_iso = data.get('selectedFecha')
        fecha_datetime = dateutil.parser.parse(fecha_iso)

        # Convertir a horario de Europa Central
        central_european_time = pytz.timezone('Europe/Berlin')  # Berlín está en la zona horaria de CET/CEST
        fecha_datetime = fecha_datetime.astimezone(central_european_time)

        # Buscar el trabajador por nombre
        trabajador = next((t for t in trabajadores if t.nombre == data.get('selectedTrabajador')), None)
        if trabajador is None:
            return jsonify({'error': 'Trabajador no encontrado'}), 404        

        horas = data.get('horasTrabajadas')
        # Se suman las horas al total de los trabajadores
        for trabajador_aux in trabajadores:
            if trabajador_aux.nombre == trabajador.nombre:
                print(fecha_datetime, flush=True)  # Debería imprimir <class 'int'> o <class 'float'>
                print(fecha_datetime.weekday(), flush=True)  # Debería imprimir <class 'int'> o <class 'float'>
                print(trabajador_aux.get_horas_dia(fecha_datetime), flush=True)  # Debería imprimir <class 'int'> o <class 'float'>

                if ((0 <= fecha_datetime.weekday() < 4) and (trabajador_aux.get_horas_dia(fecha_datetime) + horas <= 8.5)) or ((fecha_datetime.weekday() == 4 ) and (trabajador_aux.get_horas_dia(fecha_datetime) + horas <= 6)):
                    trabajador_aux.sumar_horas(data.get('horasTrabajadas'), fecha_datetime)
                else:
                    return {'status': 'Horas introducidas incorrectas.'}, 400

        if (data.get('horasTrabajadas') <= 8.5 and data.get('horasTrabajadas') > 0):
            return {'status': 'success'}, 200
        else:
            return {'status': 'El rango de horas no es válido.'}, 400
    else:
        return {'status': 'unsupported media type'}, 415

@app.route('/obtener-horas', methods=['GET'])
def obtener_horas():
    return jsonify([trabajador.to_dict() for trabajador in trabajadores])

    
if __name__ == '__main__':
    app.run(debug=True)