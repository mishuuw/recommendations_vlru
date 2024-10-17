from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/registration', methods=['GET'])
def get_data():
    # Пример данных для ответа
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

@app.route('/registration', methods=['POST'])
def post_data():
    # Получение данных из запроса
    data = request.json
    print(data, type(data), sep=' | ')
    return '200'

if __name__ == '__main__':
    app.run(debug=True)
