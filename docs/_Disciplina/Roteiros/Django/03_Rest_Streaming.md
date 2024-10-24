Para criar um aplicativo REST Django que inclua a classe `Content`, vamos seguir os passos abaixo:

### 1. **Configuração Inicial do Projeto Django**
Primeiro, você precisará criar um novo projeto Django e adicionar um app para gerenciar o conteúdo.

- Adicionar o Virtual Enviroment

ctrl +shift + P

0. Instalar Django
   ```bash
   pip install django
   ```

2. Crie um novo projeto Django:
   ```bash
   django-admin startproject streaming_platform .
   cd streaming_platform
   ```

3. Crie um app dentro do projeto:
   ```bash
   python manage.py startapp content_app
   ```
4.0. Instalar Rest Django Framework
   ```bash
   pip install djangorestframework
   ```
4.1. Adicione o app no arquivo `settings.py`:
   ```python
   INSTALLED_APPS = [
       # outros apps padrão
       'rest_framework',
       'content_app',
   ]
   ```

5. Instale o Django REST framework:
   ```bash
   pip install djangorestframework
   ```

### 2. **Definindo o Modelo `Content`**
No arquivo `content_app/models.py`, vamos definir a classe `Content` conforme o modelo proposto:

```python
from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    CONTENT_TYPES = [
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    file_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES)
    upload_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)
    status = models.CharField(max_length=20, default='published')
    creator = models.ForeignKey(User, related_name='contents', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

- **Explicação**:
  - O campo `creator` é uma ForeignKey referenciando o usuário que criou o conteúdo.
  - `content_type` define se o conteúdo é áudio ou vídeo.
  - `file_url` é o campo que contém a URL do arquivo de mídia.

### 3. **Serializador (Serializer) para `Content`**
No Django REST, precisamos de um serializador para transformar o modelo em um formato JSON que possa ser exposto via API.

Crie o arquivo `content_app/serializers.py`:

```python
from rest_framework import serializers
from .models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
```

### 4. **Views para o `Content`**
No arquivo `content_app/views.py`, crie as views utilizando o Django REST framework para expor a API.

```python
from rest_framework import viewsets
from .models import Content
from .serializers import ContentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
```

- **Explicação**:
  - `ContentViewSet` fornece as ações padrão de um ViewSet (list, create, retrieve, update, destroy).
  - `perform_create` sobrescreve o método `create` para garantir que o criador (`creator`) seja o usuário logado.

### 5. **URLs para o App**
Crie um arquivo `content_app/urls.py` e defina as rotas para o `ContentViewSet`:

```python
from rest_framework.routers import DefaultRouter
from .views import ContentViewSet

router = DefaultRouter()
router.register(r'contents', ContentViewSet)

urlpatterns = router.urls
```

Agora, no arquivo principal de URLs do projeto `streaming_platform/urls.py`, inclua o roteamento do app `content_app`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('content_app.urls')),
]
```

### 6. **Configurar Autenticação**
Como estamos utilizando o campo `creator` baseado no usuário logado, é importante configurar a autenticação no Django REST framework.

No arquivo `settings.py`, adicione a configuração para o Django REST framework:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}
```

### 7. **Migrar o Banco de Dados**
Para aplicar as mudanças do modelo no banco de dados, execute as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. **Testando a API**
Agora, você pode testar a API usando ferramentas como o **Postman** ou **curl**. Alguns endpoints disponíveis seriam:

- `GET /api/contents/`: Lista todos os conteúdos.
- `POST /api/contents/`: Cria um novo conteúdo (requer autenticação).
- `GET /api/contents/<id>/`: Detalhes de um conteúdo específico.
- `PUT /api/contents/<id>/`: Atualiza um conteúdo (requer autenticação).
- `DELETE /api/contents/<id>/`: Remove um conteúdo (requer autenticação).

### 9. **Administração no Django Admin**
Para facilitar a visualização dos conteúdos no Django Admin, você pode registrar o modelo `Content` no admin. No arquivo `content_app/admin.py`:

```python
from django.contrib import admin
from .models import Content

admin.site.register(Content)
```

Agora, ao acessar o painel de administração do Django, você poderá visualizar e gerenciar os conteúdos.

### Resumo
Essa implementação cria um app RESTful no Django com suporte à criação, leitura, atualização e exclusão (CRUD) de conteúdos, incluindo autenticação e associação com os criadores. Você pode expandir a aplicação para adicionar funcionalidades adicionais, como filtros ou buscas.
