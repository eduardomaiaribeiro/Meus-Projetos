// Chat em Tempo Real - Estrutura inicial
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.get('/', (req, res) => {
  res.send('Chat em tempo real funcionando!');
});

const PORT = process.env.PORT || 3002;
server.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));
