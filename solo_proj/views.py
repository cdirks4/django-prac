from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Song
from .serializers import SongSerializer
from rest_framework import generics, serializers
# Create your views here.


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
