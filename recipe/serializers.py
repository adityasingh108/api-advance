from django.db.models import fields
from core.models import Tag 
from rest_framework import serializers





class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name',)
        read_only_fields = ('id',)