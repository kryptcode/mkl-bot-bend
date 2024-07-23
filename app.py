from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

app = Flask(__name__)
CORS(app)

def index():
    return "Flask server is running"

@app.route('/process', methods=['POST'])
def process():
    user_input = request.json['user_input']
    result = execute_notebook(user_input)
    return jsonify(result=result)

def execute_notebook(user_input):
    # Load the notebook
    with open('chatbot.ipynb') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Add user input to notebook's first cell
    nb.cells[0].source = f"user_input = '{user_input}'\n" + nb.cells[0].source

    # Execute the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': './'}})

    # Extract the output from the last cell
    output = nb.cells[-1].outputs[0]['text']
    return output

if __name__ == '__main__':
    app.run(debug=True, port=8000)