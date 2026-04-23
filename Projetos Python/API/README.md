# FastAPI Exemplo CRUD

Este é um projeto de exemplo contendo uma API RESTful simples construída com [FastAPI](https://fastapi.tiangolo.com/) e Python. Ele foi criado como um modelo/referência para ser utilizado em repositórios Git, demonstrando operações CRUD (Create, Read, Update, Delete) básicas.

## 🚀 Tecnologias Utilizadas

*   **Python 3.8+**
*   **FastAPI**: Framework web moderno e rápido para construção de APIs.
*   **Pydantic**: Validação de dados usando type hints do Python.
*   **Uvicorn**: Servidor ASGI leve e super rápido.

## ⚙️ Estrutura do Projeto

*   `main.py`: O arquivo principal da aplicação, onde as rotas e a lógica de negócios (simulada em memória) estão definidas.
*   `requirements.txt`: Lista as dependências do projeto.
*   `.gitignore`: Arquivos e diretórios a serem ignorados pelo Git.
*   `README.md`: Este arquivo, com informações sobre o projeto.

## 🛠️ Como Executar Localmente

Siga as instruções abaixo para rodar o projeto na sua máquina.

### 1. Clone o repositório

```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DA_PASTA>
```

### 2. Crie e ative um ambiente virtual (Recomendado)

**No Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**No Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o servidor de desenvolvimento

```bash
fastapi dev main.py
```
*Ou usando uvicorn diretamente:*
```bash
uvicorn main:app --reload
```

## 📚 Documentação da API

O FastAPI gera automaticamente duas documentações interativas e muito úteis para sua API, baseadas no OpenAPI:

*   **Swagger UI**: Acesse `http://127.0.0.1:8000/docs` para uma interface de teste interativa.
*   **ReDoc**: Acesse `http://127.0.0.1:8000/redoc` para uma visão alternativa e elegante da documentação.

## 🧩 Endpoints Disponíveis

| Método | Rota             | Descrição                                 |
| :---   | :---             | :---                                      |
| GET    | `/`              | Retorna uma mensagem de boas-vindas.      |
| GET    | `/items/`        | Lista todos os itens do banco de dados.   |
| GET    | `/items/{id}`    | Busca um item específico pelo ID.         |
| POST   | `/items/`        | Cria um novo item.                        |
| PUT    | `/items/{id}`    | Atualiza as informações de um item.       |
| DELETE | `/items/{id}`    | Remove um item do banco de dados.         |

---
**Nota:** Este é apenas um projeto educacional e usa uma lista em memória para simular um banco de dados. Em produção, você deve substituir a lista `fake_db` por um banco de dados real usando ferramentas como SQLAlchemy, SQLModel, ou drivers assíncronos (como asyncpg, motor).
