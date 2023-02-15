from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from tasks.forms import UserRegistrationForm
from .views import login_view, logout_view, register



# Create your tests here.

class LoginTest(TestCase):
    def test_Login(self):        
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')        
        self.client.login(username='test_user', password='test_user')        
        response = self.client.get('/tasks/')        
        self.assertEqual(response.status_code, 200)
        
    """ def test_get_api_json(self):
        resp = self.api_client.get('/tasks/', format='json')
        self.assertValidJSONResponse(resp) """
    
    """   def test_forms(self):
        form_data = {'something': 'something'}
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid()) """
       
    def test_Logout(self):        
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user') 
        # Log in
        self.client.login(username='test_user', password='test_user') 

        # Check response code
        response = self.client.get('/tasks/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log out' in response
        self.assertFalse(b'Logout' in response.content)

        # Log out
        self.client.logout()

        # Check response code
        response = self.client.get('/logout/')
        self.assertEquals(response.status_code, 200)

        # Check 'Log in' in response
        self.assertTrue(b'Login' in response.content) # A=0000 0001, B=0000 0010, C=0000 0011    
    
    def test_login_view(self):
        client = Client()
        response = client.get('/login/')
        self.assertEqual(response.status_code, 200)
        
    def test_logout_view(self):
        client = Client()
        response = client.get('/logout/')
        self.assertEqual(response.status_code, 200) 
    
    def test_signup_view(self):
        client = Client()
        response = client.get('/signup/')
        self.assertEqual(response.status_code, 200)  
 
