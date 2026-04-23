// Gerador de Senhas Seguras - Estrutura inicial
const express = require('express');
const app = express();
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Gerador de Senhas funcionando!');
});

const PORT = process.env.PORT || 3003;
app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));
