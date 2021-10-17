from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin


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