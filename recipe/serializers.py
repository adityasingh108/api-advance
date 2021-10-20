from django.db import models
from django.db.models import fields
from django.db.models.query import QuerySet
from core.models import Ingredient, Recipe, Tag 
from rest_framework import serializers





class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name',)
        read_only_fields = ('id',)
        
        
class IngredientSerializer(serializers.ModelSerializer):
    ''' Serializer for Ingredient Objects'''
    class Meta:
        model = Ingredient
        fields = ('id','name')
        read_only_fields = ('id',)
        
        
class RecipeSerializer(serializers.ModelSerializer):
    ''' Serialize a recipe'''
    ingredients = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset =Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = Tag.objects.all(),
    )
    class Meta:
        model = Recipe 
        fields = ('id','title','ingredients','tags','time_minute','price','link',) 
        read_only_fields = ('id',)    
            