// API de Clima - Estrutura inicial
const express = require('express');
const app = express();
app.use(express.json());

app.get('/', (req, res) => {
  res.send('API de Clima funcionando!');
});

const PORT = process.env.PORT || 3004;
app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));
