from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from tasks.apps import TasksConfig
from tasks.forms import UserRegistrationForm
from django.core.exceptions import ValidationError
from .views import login_view, logout_view, register
from .serializers import UserSerializer
from kanban_app import settings
from pathlib import Path
from .models import Tasks, tasks_board
from django.utils import timezone
from datetime import timedelta
from django.apps import AppConfig


""" CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me') """
# Create your tests here.
def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)
 

class LoginTest(TestCase):
    
    """  def setUp(self):
        self.client = APIClient()
        self.User = get_user_model()
        self.valid_payload = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password': 'test_password'
        }
        self.invalid_payload = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password': 'test_password'
        }
        self.user = self.User.objects.create_user(
            username='test_user',
            email='test_user@example.com',
            password='test_password'
        )
         """
         
    def setUp(self):
        self.user = User.objects.create_user(username='testuser11', password='1234511')
        self.board = tasks_board.objects.create()
        self.task = Tasks.objects.create(
            title='test task',
            description='test description',
            priority='high',
            author=self.user,
            task_board=self.board,
            due_date=timezone.now().date() + timedelta(days=7)
        )
        
    def test_task_creation(self):
        self.assertIsInstance(self.task, Tasks)
        self.assertEqual(self.task.title, 'test task')
        self.assertEqual(self.task.description, 'test description')
        self.assertEqual(self.task.priority, 'high')
        self.assertEqual(self.task.author, self.user)
        self.assertEqual(self.task.task_board, self.board)
        self.assertEqual(self.task.due_date, timezone.now().date() + timedelta(days=7))

    """  def test_task_title(self):
        task = Tasks.objects.get(id=1)
        task.title = 'test task' # set the title attribute to 'test task'
        task.save()
        self.assertEqual(str(task.title), 'test task') """
    
    def test_Login(self):        
        self.client = Client()
        self.user = User.objects.create_user('test_user', password='test_user')        
        self.client.login(username='test_user', password='test_user')        
        response = self.client.get('/tasks/')        
        self.assertEqual(response.status_code, 200)
        
    def test_create_user(self):
        # Create a new user using the Django User model
        User = get_user_model()
        user = User.objects.create_user(
            username='test_user',
            email='test_user@example.com',
            password='test_password'
        )

        # Assert that the user was created with the correct information
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.email, 'test_user@example.com')
        self.assertTrue(user.check_password('test_password'))
        
    def test_invalid_email(self):
        invalid_email = "not_an_email"
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": invalid_email,
            "password": "password123"
        }
        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)
        
        """  def test_create_user_with_short_password(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password': '1234'  # short password
        }

        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())

        error_messages = serializer.errors.get('password', [])
        print(error_messages)
        self.assertIn('Ensure this field has at least 5 characters.', error_messages) """
        
        """ def test_email_exists_error(self):
        response = self.client.post('/api/users/', self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('/api/users/', self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(
            response.json(),
            {'email': [f'A user with email {self.invalid_payload["email"]} already exists.']}
        ) """
        
        """def test_password_min_length(self):
        serializer = UserSerializer(data={
            'email': 'test@example.com',
            'password': 'test',
            'name': 'Test Name',
        })
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)
        self.assertEqual(
            str(serializer.errors['password'][0]), 
            'Ensure this field has at least 5 characters.'
        ) """
        
        """def test_user_with_email_exists_error(self):
        #Test error returned if user with email exists.
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name',
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
        
        def test_create_token_email_not_found(self):
        #Test error returned if user not found for given email.
        payload = {'email': 'test@example.com', 'password': 'pass123'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
        def test_update_user_profile(self):
        #Test updating the user profile for the authenticated user.
        payload = {'name': 'Updated name', 'password': 'newpassword123'}

        res = self.client.patch(ME_URL, payload)

        self.user.refresh_from_db()
        self.assertEqual(self.user.name, payload['name'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        """
        
    """ def test_get_api_json(self):
        resp = self.api_client.get('/tasks/', format='json')
        self.assertValidJSONResponse(resp) """
    
    def test_forms(self):
        form_data = {'something': 'something'}
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
       
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
        
    def test_base_dir(self):
        assert settings.BASE_DIR == Path(__file__).resolve().parent.parent
        
    """  def test_allowed_hosts(self):
        for host in settings.ALLOWED_HOSTS:
            assert '.' in host """
    
    def test_debug(self):
        assert settings.DEBUG is not True or 'production' not in settings.ALLOWED_HOSTS
        
    def test_secret_key(self):
        assert settings.SECRET_KEY is not None
        
        
    def test_test_runner(self):
        assert settings.TEST_RUNNER == 'django_nose.NoseTestSuiteRunner'
        
    def test_static_url(self):
        assert settings.STATIC_URL.startswith('http') or settings.STATIC_URL.startswith('/')
        
    def test_database(self):
        if 'production' in settings.ALLOWED_HOSTS:
            assert settings.DATABASES['default']['ENGINE'] == 'django.db.backends.postgresql'
            
    """    def test_default_auto_field(self):
        config = TasksConfig('tasks', __name__)
        self.assertEqual(config.default_auto_field, 'django.db.models.BigAutoField')

    def test_name(self):
        config = TasksConfig('tasks', __name__)
        self.assertEqual(config.name, 'tasks') """
    
