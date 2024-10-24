Para criar um **Django REST API** com base nas classes que definimos no diagrama, você pode seguir os passos abaixo. Vamos estruturar o app com as classes principais.

Ps:. Não esqueça de sempre criar o ambiente virtual( **ctrl +shift + P => Python Create Enviroment** ) antes de começar qualquer projeto.


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

### 7. Criar o Models

Defina um modelo para representar um empregado:

```python
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)**
    department = models.CharField(max_length=100)**

    def __str__(self):
        return self.name
```

Agora aplique novamente o makemigrations para atualizar os models disponíveis no app e o migrate para gerar a tabela no banco

```bash
python manage.py makemigrations
python manage.py migrate
```
### 8. Adicionar ao Painel do Django-Admin

No app/admin.py import a nova classe Employee no Django-Admin

```python
from django.contrib import admin
from .models import Employee

admin.site.register(Employee)
``` 

### 9. Django-Admin

Rode novamente e entre no endereço do Django-Admin

```bash
python manage.py runserver
localhost:8000/admin
```

Para cada model adicionado devemos repetir o makemigrations  e o migrate e adicionarmos ao painel Django-Admin

### 10. Adicione o Department
```python
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```
    
    

