from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    try:
        data = request.get_json()
        if not data or 'num1' not in data or 'num2' not in data:
            return jsonify({
                'error': 'Missing required parameters: num1 and num2'
            }), 400
        
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 + num2
        
        return jsonify({
            'result': result,
            'operation': 'addition',
            'num1': num1,
            'num2': num2
        })
    except ValueError:
        return jsonify({
            'error': 'Invalid number format'
        }), 400
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/multiply', methods=['POST'])
def multiply_numbers():
    try:
        data = request.get_json()
        if not data or 'num1' not in data or 'num2' not in data:
            return jsonify({
                'error': 'Missing required parameters: num1 and num2'
            }), 400
        
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        result = num1 * num2
        
        return jsonify({
            'result': result,
            'operation': 'multiplication',
            'num1': num1,
            'num2': num2
        })
    except ValueError:
        return jsonify({
            'error': 'Invalid number format'
        }), 400
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)