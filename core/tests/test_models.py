from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.auth import get_user_model



class ModelTestCase(TestCase):
    ''' create a test class for custom user '''
    def test_create_user_with_email(self):
        ''' test with creating a user with mail '''
        email = 'aditya@mail.com'
        password = '1234'
        user = get_user_model().objects.create_user(email=email,password=password)
        
        
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
        
    def test_new_user_email_normalize(self):
        ''' test  email ''' 
        email = 'aadi@mail.com'
        user = get_user_model().objects.create_user(email,'123')
        self.assertEqual(user.email,email,email.lower)   
        
    
    def test_new_user_valid_name(self):
        ''' checking test for email '''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'1245')
            
    def test_create_super_user(self):
        email = 'aditya@mail.com'
        password = '13250'
        user = get_user_model().objects.create_superuser(email=email,password=password) 
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)        
            
            
        