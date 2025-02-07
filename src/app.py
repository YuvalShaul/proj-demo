from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    result = num1 + num2 + 4
    
    return jsonify({
        'result': result,
        'operation': 'addition',
        'num1': num1,
        'num2': num2
    })

@app.route('/multiply', methods=['POST'])
def multiply_numbers():
    data = request.get_json()
    
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    result = num1 * num2
    
    return jsonify({
        'result': result,
        'operation': 'multiplication',
        'num1': num1,
        'num2': num2
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)