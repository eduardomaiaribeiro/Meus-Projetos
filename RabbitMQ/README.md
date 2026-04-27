# Projeto de Filas com RabbitMQ

Este projeto demonstra como utilizar o RabbitMQ para o gerenciamento de filas em aplicações Python. O objetivo é fornecer um exemplo didático, seguro e pronto para ser utilizado como base em projetos que demandam comunicação assíncrona entre serviços.

## Sumário
- [Sobre o Projeto](#sobre-o-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração Segura](#configuração-segura)
- [Execução](#execução)
- [Testes](#testes)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Boas Práticas de Segurança](#boas-práticas-de-segurança)
- [Licença](#licença)

## Sobre o Projeto
Este repositório contém exemplos de produtor e consumidor de mensagens utilizando RabbitMQ. O código é estruturado para facilitar o entendimento e a reutilização, além de seguir boas práticas de segurança para evitar exposição de dados sensíveis.

## Pré-requisitos
- Python 3.8+
- Docker (opcional, para subir o RabbitMQ localmente)

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/rabbitmq-exemplo.git
   cd rabbitmq-exemplo
   ```
2. Crie um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração Segura
As credenciais de acesso ao RabbitMQ **NÃO** devem ser expostas no código-fonte. Utilize variáveis de ambiente para definir usuário, senha e host do RabbitMQ. Exemplo de arquivo `.env` (NÃO versionar este arquivo!):

```
RABBITMQ_USER=usuario
RABBITMQ_PASSWORD=senha
RABBITMQ_HOST=localhost
```

Utilize a biblioteca `python-dotenv` para carregar as variáveis de ambiente automaticamente.

## Execução
1. Suba o RabbitMQ localmente (opcional):
   ```bash
   docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
   ```
2. Execute o produtor:
   ```bash
   python producer.py
   ```
3. Execute o consumidor:
   ```bash
   python consumer.py
   ```

## Estrutura do Projeto
```
RabbitMQ/
├── consumer.py
├── producer.py
├── requirements.txt
├── .env.example
├── .gitignore
├── test_rabbitmq.py
└── README.md
```

## Testes
O projeto inclui testes unitários para garantir o correto funcionamento dos produtores e consumidores de mensagens.

Para executar os testes, utilize:

```bash
python -m unittest test_rabbitmq.py
```

Os testes utilizam mocks para simular a conexão com o RabbitMQ, não sendo necessário um servidor real para a execução dos testes.

