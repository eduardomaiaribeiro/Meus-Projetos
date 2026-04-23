// Conversor de Moedas - Estrutura inicial
const express = require('express');
const app = express();
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Conversor de Moedas funcionando!');
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));
