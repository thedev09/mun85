from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_post_request():
    try:
        data = request.json
        full_name = data.get('full_name')
        dob = data.get('dob')
        user_id = f"{full_name.replace(' ', '_')}_{dob}"
        
        numbers = [int(x) for x in data.get('data', []) if x.isdigit()]
        alphabets = [x for x in data.get('data', []) if x.isalpha()]
        highest_lowercase = max([x for x in alphabets if x.islower()], default=None)
        
        response = {
            "is_success": True,
            "user_id": user_id,
            "email_id": data.get('email_id'),
            "roll_number": data.get('roll_number'),
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase": highest_lowercase
        }
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def process_get_request():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
