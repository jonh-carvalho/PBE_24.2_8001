
Para criar um **Django REST API** com base nas classes que definimos no diagrama, você pode seguir os passos abaixo. Vamos estruturar o app com as classes principais.

### 1. **Configuração Inicial do Projeto Django**

Certifique-se de ter o Django e o Django REST Framework instalados. Se ainda não estiverem instalados, execute:

```bash
pip install django
```

#### Criação do Projeto e App

```bash
django-admin startproject project

python manage.py startapp app
```

### 2. **Configurar o Projeto Django**

No arquivo `settings.py` do projeto, adicione o `rest_framework` e o novo app `activities` na lista de aplicativos instalados:

```python
INSTALLED_APPS = [
    # Apps Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]
```

### 3. **Criar as Migrations e Migrar o Banco de Dados**

Agora que o modelo está pronto, criamos as migrações e aplicamos ao banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Iniciar o servidor do Django:

```bash
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/api/` para ver os endpoints disponíveis para criar e visualizar atividades, tipos de atividades, métricas e histórico.

### 5. Criar super Usuário

```
python manage.py createsuperuser
```

### 6. Django-Admin

```
localhost:8000/admin
```
