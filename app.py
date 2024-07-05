from flask import Flask, request, jsonify
from flask_cors import CORS
import okan

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = okan.get_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port = 8000)
