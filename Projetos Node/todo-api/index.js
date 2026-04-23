// To-Do List API - Estrutura inicial
const express = require('express');
const app = express();
app.use(express.json());

app.get('/', (req, res) => {
  res.send('API de Tarefas funcionando!');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));
