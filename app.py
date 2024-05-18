from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Esto permitirá todas las solicitudes de todos los orígenes

@app.route('/log', methods=['POST'])
def log_message():
    if request.is_json:
        data = request.get_json()
        print(f"Received selectedTrabajador: {data.get('selectedTrabajador')}", flush=True)
        print(f"Received horasTrabajadas: {data.get('horasTrabajadas')}", flush=True)

        if (data.get('horasTrabajadas') < 8 and data.get('horasTrabajadas') > 0):
            return {'status': 'success'}, 200
        else:
            return {'status': 'El rango de horas no es válido.'}, 400
    else:
        return {'status': 'unsupported media type'}, 415

if __name__ == '__main__':
    app.run(debug=True)