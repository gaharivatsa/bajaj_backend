from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        data = request.json.get('data', [])
        if not isinstance(data, list):
            return jsonify({"is_success": False, "message": "Invalid input format"}), 400
        
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_alphabet = max(alphabets, key=lambda x: x.lower()) if alphabets else []

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999", 
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
