# FastAPI 2FA Authentication API

Este projeto é uma API em Python utilizando FastAPI com autenticação 2FA (Two-Factor Authentication), pronta para deploy e exposição no GitHub.

## Recursos
- Cadastro e login de usuários
- Autenticação com senha e 2FA (TOTP)
- Endpoints protegidos
- Testes automatizados

## Como rodar localmente

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute a aplicação:
   ```bash
   uvicorn app.main:app --reload
   ```

## Testes

```bash
pytest
```


## Como testar o 2FA na prática

1. **Obtenha o segredo 2FA:**
    - Faça uma requisição GET para `/2fa-secret?username=user@example.com`.
    - O retorno será um segredo base32, por exemplo: `JBSWY3DPEHPK3PXP`.

2. **Gere o QR Code:**
    - Use um site como [otpauth.net](https://otpauth.net/generate) ou um gerador de QR Code para TOTP.
    - Formato da URL para QR Code:
       ```
       otpauth://totp/NomeApp:user@example.com?secret=SEU_SEGREDO&issuer=NomeApp
       ```
       Substitua `SEU_SEGREDO` pelo segredo retornado.

3. **Escaneie o QR Code:**
    - Use um app autenticador (Google Authenticator, Authy, Microsoft Authenticator, etc) para escanear o QR Code.

4. **Valide o token:**
    - Gere um token no app autenticador.
    - Envie uma requisição POST para `/2fa-verify` com os parâmetros `username` e `token`.
    - Exemplo:
       ```json
       {
          "username": "user@example.com",
          "token": "123456"
       }
       ```
    - Se o token estiver correto, a resposta será:
       ```json
       { "msg": "2FA verificado com sucesso" }
       ```

## Rotas de teste

- `/public`: rota aberta para qualquer usuário.
- `/protected`: rota protegida, exige autenticação via token.

## Exemplo de uso
Veja exemplos de requisições no arquivo `tests/test_main.py`.

## 📝 Como acessar o Swagger (OpenAPI)

Após iniciar o servidor, acesse a documentação interativa gerada automaticamente pelo Swagger UI:

- Abra o navegador e vá para: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Você poderá:
- Visualizar todos os endpoints disponíveis
- Testar requisições diretamente pela interface
- Ver exemplos de request/response
- Conferir descrições, parâmetros e modelos de dados

Se preferir, utilize também a documentação alternativa gerada pelo ReDoc em [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

---

> Substitua variáveis sensíveis e configure o ambiente conforme necessário.
