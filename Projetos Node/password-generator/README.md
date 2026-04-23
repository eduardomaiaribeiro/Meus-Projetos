# Gerador de Senhas Seguras

API para geração de senhas seguras e personalizáveis.

## Funcionalidades
- Gera senhas aleatórias com diferentes níveis de complexidade
- Parâmetros para tamanho, uso de símbolos, números, letras maiúsculas/minúsculas

## Como usar
1. Instale as dependências:
	```bash
	npm install
	```
2. Inicie o servidor:
	```bash
	npm start
	```
3. Acesse: http://localhost:3003

## Rotas principais
- `GET /generate?length=12&symbols=true&numbers=true` – Gera uma senha de 12 caracteres com símbolos e números
