const express = require('express');
const bodyParser = require('body-parser');
const { execFile } = require('child_process');
const path = require('path');

const app = express();
const port = 8000;

app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.send('Chatbot backend is running!');
});

app.post('/run-notebook', (req, res) => {
  const userInput = req.body.userInput; // Get user input from the request body
  const notebookPath = path.join(__dirname, 'mkl.ipynb');

  execFile('python', ['execute_notebook.py', notebookPath, userInput], (error, stdout, stderr) => {
    if (error) {
      res.status(500).send({ error: error.message });
      return;
    }

    if (stderr) {
      console.error(`Stderr: ${stderr}`);
    }

    try {
      const result = JSON.parse(stdout);
      res.send(result);
    } catch (parseError) {
      res.status(500).send({ error: 'Failed to parse Python script output' });
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});