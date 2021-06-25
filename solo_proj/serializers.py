from django.db import models
from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    view_name = 'song',
    many = False,
    read_only = True

    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'link')
