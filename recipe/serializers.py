from django.db import models
from django.db.models import fields
from core.models import Ingredient, Tag 
from rest_framework import serializers





class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name',)
        read_only_fields = ('id',)
        
        
class IngredientSerializer(serializers.ModelSerializer):
    ''' Serializer for Ingredient Oobjects'''
    class Meta:
        model = Ingredient
        fields = ('id','name')
        read_only_fields = ('id',)
            