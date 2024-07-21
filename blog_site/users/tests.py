from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile

class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('register')
    
    def test_register_get(self):
        """Test GET request to register view"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
    
    def test_register_post_valid(self):
        """Test POST request to register view with valid data"""
        response = self.client.post(self.url, {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertRedirects(response, reverse('login'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Account created! You can login now')
    
    def test_register_post_invalid(self):
        """Test POST request to register view with invalid data"""
        response = self.client.post(self.url, {
            'username': 'Newuser',
            'email': 'Newuser345@gmail.com',
            'password1': 'testing321',
            'password2': 'testing321'
        })
        self.assertEqual(response.status_code, 200)  # Re-render the form
        self.assertTemplateUsed(response, 'users/register.html')