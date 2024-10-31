Para habilitar o *Cross-Origin Resource Sharing* (CORS) no Django, você pode utilizar o pacote `django-cors-headers`. Ele permite configurar quais domínios externos têm permissão para acessar sua API, especialmente útil para permitir que um front-end hospedado em um domínio diferente consuma dados da sua aplicação Django. Veja o passo a passo:

### Passo 1: Instalar o `django-cors-headers`

No terminal, execute:

```bash
pip install django-cors-headers
```

### Passo 2: Configurar o `django-cors-headers`

No arquivo `settings.py`, adicione `'corsheaders'` à lista de aplicativos instalados:

```python

INSTALLED_APPS = [
    ...,
    'corsheaders',
    ...,
]
```

### Passo 3: Adicionar o middleware

Adicione o middleware `CorsMiddleware` logo no início da lista de *middlewares* em `settings.py`:

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...,
]
```

### Passo 4: Configurar os domínios permitidos

Existem duas opções principais para configurar os domínios que podem acessar sua API:

1. **Permitir todos os domínios** (não recomendado para produção):
   
```python
   CORS_ALLOW_ALL_ORIGINS = True
```

2. **Permitir domínios específicos**:
   
```python
   CORS_ALLOWED_ORIGINS = [
       "https://example.com",
       "https://sub.example.com",
       "http://localhost:3000",  # Exemplo para um app local
   ]
```

### Passo 5: Outras configurações úteis

- **Permitir credenciais (cookies e autenticação)**:

```python
   CORS_ALLOW_CREDENTIALS = True
```

- **Permitir cabeçalhos específicos**:

```python
   CORS_ALLOW_HEADERS = ['content-type', 'authorization']
```

Com isso, seu Django estará configurado para aceitar requisições *cross-origin* de acordo com as permissões definidas.