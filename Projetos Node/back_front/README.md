
# Projeto Node.js Backend + Frontend

Este projeto é um exemplo completo de aplicação web, integrando um backend em Node.js (usando Express) e um frontend simples em HTML, CSS e JavaScript. O objetivo é demonstrar como estruturar e integrar as duas camadas em um único repositório, pronto para ser publicado no GitHub.

## O que este projeto faz?

- O **backend** serve os arquivos estáticos do frontend e expõe uma API REST simples.
- O **frontend** consome a API e exibe a resposta na interface.
- Ideal para estudos, testes, prototipação e como ponto de partida para projetos maiores.

### Funcionalidades
- Servir arquivos estáticos do frontend via Express
- Endpoint de API `/api/hello` que retorna uma mensagem JSON
- Exemplo de chamada à API usando JavaScript no frontend

## Estrutura

- `backend/`: Servidor Node.js com Express
   - `index.js`: Código principal do backend
   - `package.json`: Dependências e scripts
   - `swagger.json`: Documentação da API no padrão OpenAPI/Swagger
- `frontend/`: Arquivos estáticos (HTML, CSS, JS)
   - `index.html`, `style.css`, `script.js`

## Como rodar

1. Instale as dependências do backend:
   ```bash
   cd backend
   npm install
   npm start
   ```
2. Acesse o frontend em [http://localhost:3000](http://localhost:3000)

## Publicação

Basta inicializar um repositório Git e fazer o push para o GitHub:

```bash
git init
git add .
git commit -m "Projeto inicial"
git branch -M main
git remote add origin https://github.com/seu-usuario/seu-repo.git
git push -u origin main
```

---

## Documentação da API (Swagger)

O backend expõe a seguinte API:

```yaml
openapi: 3.0.0
info:
   title: Exemplo API Backend
   version: 1.0.0
   description: API simples para demonstração de integração backend/frontend.
servers:
   - url: http://localhost:3000
      description: Servidor local
paths:
   /api/hello:
      get:
         summary: Retorna uma mensagem de saudação
         responses:
            '200':
               description: Mensagem de saudação
               content:
                  application/json:
                     schema:
                        type: object
                        properties:
                           message:
                              type: string
                              example: Hello from backend!
```

O arquivo completo está em `backend/swagger.json`.
