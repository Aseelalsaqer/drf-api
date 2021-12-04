from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, permissions, serializers
from .serializer import SnackSerializer 
from .models import Snack
from .permissions import IsAuthorOrReadOnly , IsAuthenticatedOrReadOnly

# Create your views here.
class SnackList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer 

class SnackDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer