# API de Clima

API que retorna informações do clima consumindo dados do OpenWeatherMap.

## Funcionalidades
- Consulta o clima atual de uma cidade
- Consome dados de uma API pública de clima

## Como usar
1. Instale as dependências:
	```bash
	npm install
	```
2. Inicie o servidor:
	```bash
	npm start
	```
3. Acesse: http://localhost:3004

## Rotas principais
- `GET /weather?city=Sao Paulo` – Retorna o clima atual de São Paulo
