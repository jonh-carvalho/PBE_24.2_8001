from django.shortcuts import render

from rest_framework import viewsets
from .models import Content
from .serializers import ContentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)# Create your views here.
