# Autenticação

Para autenticar no Django REST Framework (DRF) e consumir a API como um usuário logado, você pode usar várias abordagens de autenticação, como:

1. **Autenticação via Token**.
2. **Autenticação via Sessão/Cookie (principalmente para navegadores)**.
3. **Autenticação JWT** (JSON Web Token).

## Autenticação via Token

Abaixo, vamos ver como configurar a **Autenticação via Token** no Django e como consumir a API com um token de autenticação.

### Passo 1: Configurar Autenticação por Token no Django REST Framework

1\. Instale o pacote `djangorestframework` (caso ainda não tenha):

```bash
    pip install djangorestframework
```

2\. Instale o pacote `djangorestframework-authtoken`, necessário para gerar e gerenciar tokens de autenticação:

```bash
   pip install djangorestframework-authtoken
```

3\. Adicione `rest_framework` e `rest_framework.authtoken` ao `INSTALLED_APPS` no seu `settings.py`:

```python
   INSTALLED_APPS = [
       # Outros apps
       'rest_framework',
       'rest_framework.authtoken',
   ]
```

4\. Configure o Django REST Framework para usar a autenticação por token:

```python
   # settings.py

   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework.authentication.TokenAuthentication',
       ],
       'DEFAULT_PERMISSION_CLASSES': [
           'rest_framework.permissions.IsAuthenticated',
       ],
   }
```

5\. Execute a migração para criar as tabelas necessárias:

```bash
   python manage.py migrate
```

### Passo 2: Gerar Tokens de Autenticação

Crie uma URL para o endpoint de obtenção de tokens de autenticação. No seu `urls.py`, adicione:

```python
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Outras rotas
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
```

Com isso, os usuários poderão obter tokens enviando uma requisição `POST` com suas credenciais (usuário e senha) para `api/token/`.

### Passo 3: Obter o Token de Autenticação

Para obter o token, você pode usar o `curl`, Postman, ou qualquer cliente HTTP. No Postman, por exemplo:

- Envie uma requisição `POST` para `http://localhost:8000/api/token/`.
- No corpo da requisição (`body`), envie as credenciais como `x-www-form-urlencoded`:

```plaintext
   username: seu_usuario
   password: sua_senha
```

A resposta será o token de autenticação do usuário, por exemplo:

```json
{
    "token": "c1c82e123abc123abcde4567def01234abcd5678"
}
```

### Passo 4: Usar o Token para Consumir a API

Agora, ao consumir a API, adicione o token ao cabeçalho de autenticação (`Authorization`) usando o formato `Token <token>`.

#### Exemplo de Consumo no Postman

1. Acesse qualquer endpoint da API protegido, como `http://localhost:8000/api/contents/`.

2. No cabeçalho (`Headers`), adicione:

```plaintext
   Authorization: Token c1c82e123abc123abcde4567def01234abcd5678
```

Com esse cabeçalho, o Django REST Framework identificará o usuário autenticado e permitirá o acesso aos recursos da API, desde que o usuário tenha as permissões necessárias.

### Alternativa: Uso no Frontend com JavaScript (Fetch API)

Se estiver consumindo a API com JavaScript no frontend, o código para usar o token ficaria assim:

```javascript
fetch('http://localhost:8000/api/contents/', {
    method: 'GET',
    headers: {
        'Authorization': 'Token c1c82e123abc123abcde4567def01234abcd5678',
        'Content-Type': 'application/json'
    }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

### Considerações Finais

- **Manter o Token Seguro**: Evite expor o token em locais de fácil acesso ou em JavaScript sem proteção.
- **Token Expirável (opcional)**: O pacote `django-rest-framework-simplejwt` oferece tokens JWT com tempo de expiração configurável, se precisar de tokens mais seguros.

Esse fluxo permite que seu app Django autentique usuários e proteja rotas da API, limitando o acesso a quem possui um token válido.
