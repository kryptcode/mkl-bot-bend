from flask import Flask, request, jsonify
import okan  # Replace with your chatbot module

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = your_chatbot_module.get_response(user_input)  # Adjust based on your chatbot's function
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
