from flask import Flask, request, jsonify, render_template
from db import ejecutar_funcion
app = Flask(__name__)

# La función 'ejecutar_funcion' debe existir previamente en tu base de datos o en tu código.
# Este endpoint solo la llama, no la crea.
@app.route('/api/funcion/funcion', methods=['POST'])
def api_funcion():
    nombre_funcion = request.json.get('nombre_funcion')
    parametros = request.json.get('parametros', [])
    try:
        resultado = ejecutar_funcion(nombre_funcion, parametros)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
