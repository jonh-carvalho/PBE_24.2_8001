from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Content
from .serializers import ContentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    #permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Content.objects.all()
      
        # Filtro por tipo de conteúdo (audio/video)
        content_type = self.request.query_params.get('content_type')
        if content_type in [choice[0] for choice in Content.CONTENT_TYPES]:
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
        
