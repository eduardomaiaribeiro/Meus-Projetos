# To-Do List API

API REST para gerenciamento de tarefas (CRUD) usando Node.js e Express.

## Funcionalidades
- Criar, listar, atualizar e remover tarefas
- Cada tarefa possui título, descrição e status (pendente/concluída)

## Como usar
1. Instale as dependências:
	```bash
	npm install
	```
2. Inicie o servidor:
	```bash
	npm start
	```
3. Acesse: http://localhost:3000

## Rotas principais
- `GET /tasks` – Lista todas as tarefas
- `POST /tasks` – Cria uma nova tarefa
- `PUT /tasks/:id` – Atualiza uma tarefa
- `DELETE /tasks/:id` – Remove uma tarefa
