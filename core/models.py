from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):
    '''class for user manager '''
    def create_user(self,email,password=None,**extra_fields):
        ''' create user '''
        if not email:
            raise ValueError('User must have email address')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,email,password):
        '''Creating super user'''
        user = self.create_user(email,password)
        
        
        user.is_superuser = True
        user.is_staff = True
        
        user.save(using= self._db)
        return user
        
    
class User(AbstractBaseUser,PermissionsMixin):
    '''creating the class for user registration '''
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS =
    
    
class Tag(models.Model):
    ''' model for tag'''
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)  
    
    
    def __str__(self):
        return self.name 
    
class Ingredient(models.Model):
    ''' Ingredient to be used in recipe''' 
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)  
    
    
    def __str__(self):
        return self.name  



class Recipe(models.Model):
    ''' recipe Object'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    time_minute = models.IntegerField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    link = models.CharField(max_length=255,blank=True)
    ingredients = models.ManyToManyField('Ingredient') 
    tags = models.ManyToManyField('Tag')
    
    
    
    def __str__(self):
        return self.title    