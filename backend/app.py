from flask import Flask, request, jsonify  # Added jsonify to the import
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Enable CORS for all domains on all routes with allowed headers
CORS(app, resources={r"/*": {"origins": "*"}}, headers=['Content-Type'])

@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    numbers = [x for x in data if x.isdigit()]  # Collect numbers
    alphabets = [x for x in data if x.isalpha()]  # Collect alphabets
    highest_alphabet = max(alphabets, key=lambda x: x.lower(), default=None)  # Find highest alphabet

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",  # Replace with your info
        "email": "john@xyz.com",         # Replace with your info
        "roll_number": "ABCD123",        # Replace with your roll number
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": [highest_alphabet] if highest_alphabet else []
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
