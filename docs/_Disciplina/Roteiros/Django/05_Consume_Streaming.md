Para acessar a API criada no Django REST framework, siga os passos abaixo. A API está acessível através de rotas prefixadas por `api/` conforme configurado no arquivo `urls.py`. Você pode testar a API usando ferramentas como **Postman**, **Insomnia**, ou até mesmo **cURL** no terminal.

### 1. **URLs Principais da API**
Com base na configuração do roteamento, as URLs disponíveis são:

- **Listar todos os conteúdos**: `GET /api/contents/`
- **Criar um novo conteúdo**: `POST /api/contents/` (Requer autenticação)
- **Ver detalhes de um conteúdo específico**: `GET /api/contents/<id>/`
- **Atualizar um conteúdo**: `PUT /api/contents/<id>/` (Requer autenticação)
- **Deletar um conteúdo**: `DELETE /api/contents/<id>/` (Requer autenticação)

### 2. **Acessando via Navegador**
Se você estiver rodando o servidor de desenvolvimento do Django localmente, use o comando:

```bash
python manage.py runserver
```

Agora, você pode acessar a API via navegador (ou Postman) em:

- **http://127.0.0.1:8000/api/contents/** — para listar todos os conteúdos.

O Django REST framework oferece uma interface de navegação de API embutida. Se você acessar a API pelo navegador, verá uma interface amigável onde pode visualizar, criar, editar e excluir registros.

### 3. **Autenticação de Usuário**
Alguns endpoints (como criar, atualizar e deletar conteúdo) requerem que o usuário esteja autenticado. Existem várias maneiras de se autenticar:

#### a) **Autenticação de Sessão**
Se você estiver logado como usuário no Django Admin, pode testar a API no mesmo navegador porque as credenciais de sessão serão reutilizadas.

1. Acesse o Django Admin em `http://127.0.0.1:8000/admin/`.
2. Faça login com um superusuário.
3. Agora, vá para `http://127.0.0.1:8000/api/contents/` e você poderá fazer operações autenticadas diretamente no navegador.

#### b) **Autenticação Básica (Basic Auth)**
Para testar com ferramentas como **Postman** ou **cURL**, você pode usar autenticação básica.

**No Postman**:
1. No cabeçalho da requisição, vá até a aba "Authorization".
2. Selecione o tipo "Basic Auth".
3. Insira seu **username** e **password**.

**Com cURL**:
Você pode usar o seguinte comando no terminal para criar um novo conteúdo (por exemplo):

```bash
curl -X POST http://127.0.0.1:8000/api/contents/ \
  -H "Content-Type: application/json" \
  -u <username>:<password> \
  -d '{
        "title": "Sample Video",
        "description": "A sample video description",
        "file_url": "http://example.com/sample.mp4",
        "thumbnail_url": "http://example.com/thumb.jpg",
        "content_type": "video",
        "is_public": true
      }'
```

### 4. **Exemplos de Requisições**

#### a) **GET - Listar todos os conteúdos**
Você pode listar todos os conteúdos disponíveis com a seguinte requisição:

**Com cURL**:
```bash
curl -X GET http://127.0.0.1:8000/api/contents/
```

#### b) **POST - Criar um novo conteúdo**
Para criar um novo conteúdo, você precisa estar autenticado e fornecer os dados adequados:

**No Postman**:
1. Defina o método como `POST`.
2. No campo URL, insira `http://127.0.0.1:8000/api/contents/`.
3. Vá até a aba "Body" e selecione `raw` com o tipo `JSON`, e insira algo como:
   ```json
   {
       "title": "My Video",
       "description": "A video description",
       "file_url": "http://example.com/video.mp4",
       "thumbnail_url": "http://example.com/thumbnail.jpg",
       "content_type": "video",
       "is_public": true
   }
   ```
4. Envie a requisição.

#### c) **PUT - Atualizar um conteúdo**
Atualizar um conteúdo requer que você esteja autenticado e seja o criador do conteúdo.

**Com cURL**:
```bash
curl -X PUT http://127.0.0.1:8000/api/contents/<id>/ \
  -H "Content-Type: application/json" \
  -u <username>:<password> \
  -d '{
        "title": "Updated Video Title",
        "description": "Updated description"
      }'
```

#### d) **DELETE - Remover um conteúdo**
Para deletar um conteúdo (somente se você for o criador ou administrador):

**Com cURL**:
```bash
curl -X DELETE http://127.0.0.1:8000/api/contents/<id>/ \
  -u <username>:<password>
```

### 5. **Filtros e Busca**
Você pode adicionar filtros de busca com base nos campos do modelo `Content` (como `title`, `content_type`, etc.), integrando a funcionalidade de filtros no Django REST framework usando `DjangoFilterBackend`.

Exemplo de adição de filtro para busca por título ou tipo de conteúdo:

**No `views.py`**:
```python
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'content_type']
```

Agora você pode buscar por título ou tipo de conteúdo:

- `GET /api/contents/?search=My Video`
- `GET /api/contents/?search=audio`

### Resumo:
1. Acesse a API via `http://127.0.0.1:8000/api/contents/`.
2. Utilize autenticação para operações que requerem login (POST, PUT, DELETE).
3. Use ferramentas como Postman ou cURL para testar os endpoints.
4. Adicione filtros ou funcionalidades adicionais conforme necessário.

Assim, a API está configurada e pronta para ser consumida por frontends, aplicativos móveis ou outras aplicações REST.