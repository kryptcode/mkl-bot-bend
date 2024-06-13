import sys
import json
import nbformat
from nbclient import NotebookClient
import asyncio

# Set the event loop policy for Windows
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def execute_notebook(notebook_path, user_input):
    with open(notebook_path) as f:
        notebook = nbformat.read(f, as_version=4)

    # Inject user input into the notebook
    notebook.cells[0] = nbformat.v4.new_code_cell(source=f"user_input = '{user_input}'")

    client = NotebookClient(notebook)

    try:
        client.execute()
    except Exception as e:
        return {'output': '', 'error': str(e)}

    # Collect output from the notebook cells
    output = []
    for cell in notebook.cells:
        if cell.cell_type == 'code':
            for output_item in cell.outputs:
                if 'text' in output_item:
                    output.append(output_item['text'])
                if 'data' in output_item and 'text/plain' in output_item['data']:
                    output.append(output_item['data']['text/plain'])

    return {'output': '\n'.join(output), 'error': None}

if __name__ == "__main__":
    notebook_path = sys.argv[1]
    user_input = sys.argv[2]
    result = execute_notebook(notebook_path, user_input)
    print(json.dumps(result))
