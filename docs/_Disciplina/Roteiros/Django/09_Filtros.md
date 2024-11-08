# 09 Filtros

Para implementar o filtro você pode definir manualmente o filtro na sua view, utilizando parâmetros de query (`query params`) para filtrar o `content_type` diretamente na sua consulta.

## Exemplo de View com Filtro Manual

Aqui está uma implementação usando uma `ListAPIView`, onde o filtro é feito verificando o valor do parâmetro `content_type` na requisição.

```python
# app/views.py

from rest_framework import generics
from rest_framework.response import Response
from .models import Content
from .serializers import ContentSerializer

class ContentListView(generics.ListAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
        queryset = Content.objects.all()
        content_type = self.request.query_params.get('content_type')

        if content_type in [choice[0] for choice in Content.CONTENT_TYPE_CHOICES]:
            queryset = queryset.filter(content_type=content_type)
      
        return queryset
```

### Explicação

1. **Recuperação do Parâmetro de Query**: A função `get_queryset()` verifica se o parâmetro `content_type` foi enviado na requisição (`self.request.query_params.get('content_type')`).
2. **Validação do Parâmetro**: A verificação `if content_type in [choice[0] for choice in Content.CONTENT_TYPE_CHOICES]` assegura que o valor de `content_type` corresponde a uma das escolhas válidas definidas no modelo `Content`.
3. **Aplicação do Filtro**: Se o parâmetro `content_type` for válido (`audio` ou `video`), ele será aplicado ao queryset usando `filter(content_type=content_type)`.

### Testando o Filtro

Você pode acessar os endpoints da seguinte forma:

- Para filtrar apenas conteúdos de áudio:

```bash
http://localhost:8000/api/contents/?content_type=audio
```

- Para filtrar apenas conteúdos de vídeo:

```bash
http://localhost:8000/api/contents/?content_type=video
```

## Filtros para os Campos Title e Description

Para adicionar filtros pelos campos `title` e `description`, você pode usar o mesmo método de query params dentro da sua view, permitindo que os usuários filtrem os conteúdos com base em partes do título ou descrição. No Django, você pode usar consultas `__icontains` para fazer uma busca parcial e insensível a maiúsculas e minúsculas.

### Atualizando a View para Filtrar `title` e `description`

Vamos modificar a função `get_queryset` para incluir os parâmetros `title` e `description`:

```python
# app/views.py

from rest_framework import generics
from .models import Content
from .serializers import ContentSerializer

class ContentListView(generics.ListAPIView):
    serializer_class = ContentSerializer

    def get_queryset(self):
        queryset = Content.objects.all()
      
        # Filtro por tipo de conteúdo (audio/video)
        content_type = self.request.query_params.get('content_type')
        if content_type in [choice[0] for choice in Content.CONTENT_TYPE_CHOICES]:
            queryset = queryset.filter(content_type=content_type)

        # Filtro por título (parcial e insensível a maiúsculas/minúsculas)
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        # Filtro por descrição (parcial e insensível a maiúsculas/minúsculas)
        description = self.request.query_params.get('description')
        if description:
            queryset = queryset.filter(description__icontains=description)

        return queryset
```

### Explicações

1. **Filtro de `content_type`**: O mesmo que antes, filtrando apenas se `content_type` está presente nos valores válidos.
2. **Filtro de `title`**: Se o parâmetro `title` é passado, a consulta `filter(title__icontains=title)` procura por conteúdos que contenham o valor de `title` em qualquer parte do título, sem diferenciar maiúsculas de minúsculas.
3. **Filtro de `description`**: O mesmo princípio é aplicado ao parâmetro `description` com `filter(description__icontains=description)`.

### Teste o Filtro

Agora você pode usar os parâmetros `content_type`, `title` e `description` para filtrar os conteúdos:

- Para buscar conteúdos de áudio com "Music" no título:

```bash
http://localhost:8000/api/contents/?content_type=audio&title=Music
```

- Para buscar conteúdos com "Tutorial" na descrição:

```bash
http://localhost:8000/api/contents/?description=Tutorial
```

- Para combinar filtros (exemplo, vídeos com "Adventure" no título):

```bash
http://localhost:8000/api/contents/?content_type=video&title=Adventure
```

Esse código permite aplicar os filtros `title` e `description` de forma simples e diretamente na view.
