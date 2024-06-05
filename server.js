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
  const notebookPath = path.join(__dirname, 'chatbot.ipynb');

  execFile('python', ['execute_notebook.py', notebookPath], (error, stdout, stderr) => {
    if (error) {
      res.status(500).send({ error: error.message });
      return;
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
