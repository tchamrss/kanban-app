from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User


# Create your tests here.

class LoginTest(TestCase):
    def Login_test(self):        
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')        
        self.client.login(username='test_user', password='test_user')        
        response = self.client.get('/tasks/')        
        self.assertEqual(response.status_code, 200)
       
    def Logout_test(self):        
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user') 
        # Log in
        self.client.login(username='test_user', password='test_user') 

        # Check response code
        response = self.client.get('/tasks/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertTrue('Log out' in response.content)

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/logout/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue('Log in' in response.content)       
