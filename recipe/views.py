from rest_framework import filters, viewsets,mixins,status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from core.models import Ingredient, Recipe, Tag
from recipe import serializers
import recipe



class TagViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    ''' manage tags in database'''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    
    
    
    def get_queryset(self):
        ''' return object for the current authenciated user only'''
        return self.queryset.filter(user = self.request.user).order_by('-name')
    
    
    def perform_create(self, serializer):
        ''' craete a new tag'''
        serializer.save(user=self.request.user)
        
 
    
class IngredientViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin):
    '''Manage ingredients in the database '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer 
    
    
    def get_queryset(self):
        '''return object for the current authenciated user only'''
        return  self.queryset.filter(user = self.request.user).order_by('-name')   

    def perform_create(self, serializer):
        ''' Create Ingredient'''
        serializer.save(user = self.request.user)


class RecipeViewset(viewsets.ModelViewSet):
    '''mange recipe in the database ''' 
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tags','ingredients']
    
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    
    def get_serializer_class(self):
        ''' return appropiate serilizer class '''
        if self.action == 'retrieve':
            return serializers.RecipeDetailSrializer
        elif self.action == 'upload-image':
            return serializers.ReceipeImageSerilizer
            
        
        return self.serializer_class
    
    def perform_create(self, serializer):
        ''' Create a new receipe '''
        serializer.save(user = self.request.user)
        
    
    @action(methods=['POST'],detail=True ,url_path='upload-image')
    def upload_image(self,request,pk=True):
        ''' upload an image to receipe'''
        recipe = self.get_object()
        serializers = self.get_serializer(
            recipe,
            data = request.data
        )    
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
         
    
    
    
    
            
         
     