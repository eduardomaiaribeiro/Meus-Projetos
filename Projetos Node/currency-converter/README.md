# Conversor de Moedas

API para conversão de moedas utilizando dados de uma API externa.

## Funcionalidades
- Converte valores entre diferentes moedas
- Consome taxas de câmbio em tempo real de uma API pública

## Como usar
1. Instale as dependências:
	```bash
	npm install
	```
2. Inicie o servidor:
	```bash
	npm start
	```
3. Acesse: http://localhost:3001

## Rotas principais
- `GET /convert?from=USD&to=BRL&amount=100` – Converte 100 dólares para reais
