import nbformat

# Path to your notebook file
notebook_path = 'mkl.ipynb'

# Load the notebook
with open(notebook_path) as f:
    notebook = nbformat.read(f, as_version=4)

# Add a new cell at the beginning of the notebook to define `user_input`
new_cell = nbformat.v4.new_code_cell(source="user_input = ''")

# Insert the new cell at the beginning
notebook.cells.insert(0, new_cell)

# Identify and modify cells that use input()
for cell in notebook.cells:
    if cell.cell_type == 'code' and 'input(' in cell.source:
        cell.source = cell.source.replace(
            'input("You: ")', 'user_input'
        )

# Save the modified notebook
with open(notebook_path, 'w') as f:
    nbformat.write(notebook, f)

print("Notebook has been modified successfully.")
