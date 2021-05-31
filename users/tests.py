from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class RegisterPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_page_code(self):
        response = self.client.get('/user/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_signup_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    

