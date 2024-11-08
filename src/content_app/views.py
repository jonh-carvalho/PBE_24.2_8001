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
        content_type = self.request.query_params.get('content_type')
        
        if content_type in [choice[0] for choice in Content.CONTENT_TYPES]:
            queryset = queryset.filter(content_type=content_type)

        return queryset
        
