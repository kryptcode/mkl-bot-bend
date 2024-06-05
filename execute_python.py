import sys
import json
import nbformat
from nbclient import NotebookClient

def execute_notebook(notebook_path):
    with open(notebook_path) as f:
        notebook = nbformat.read(f, as_version=4)

    client = NotebookClient(notebook)
    client.execute()

    output = []
    for cell in notebook.cells:
        if cell.cell_type == 'code':
            for output_item in cell.outputs:
                if 'text' in output_item:
                    output.append(output_item['text'])
                if 'data' in output_item and 'text/plain' in output_item['data']:
                    output.append(output_item['data']['text/plain'])

    return '\n'.join(output)

if __name__ == "__main__":
    notebook_path = sys.argv[1]
    output = execute_notebook(notebook_path)
    result = {
        'output': output,
        'error': None
    }
    print(json.dumps(result))
