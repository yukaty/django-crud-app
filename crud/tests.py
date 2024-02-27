from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

# Access the top page without login
class TestTopPage(TestCase):
    def test_top_page_status_code(self):
        response = self.client.get(reverse('top'))
        self.assertEqual(response.status_code, 200)

    def test_top_page_template(self):
        response = self.client.get(reverse('top'))
        self.assertTemplateUsed(response, 'top.html')

# Login and logout
class TestLogin(TestCase):

    def setUp(self):
        # Create a user for testing login/logout
        self.username = 'testuser'
        self.password = 'testpassword123'
        self.user = User.objects.create_user(self.username, password=self.password)

    def test_login(self):
        response = self.client.login(username=self.username, password=self.password)
        self.assertTrue(response)

    def test_logout(self):
        # Log in the user
        self.client.login(username=self.username, password=self.password)

        # Log out using a POST request which is the expected method by Django's default LogoutView
        response = self.client.post(reverse('logout'))
        # Verify the response redirects to the top page (as specified in LOGOUT_REDIRECT_URL)
        self.assertRedirects(response, reverse('top'))

    def test_logout_GET(self):
        # Log in the user
        self.client.login(username=self.username, password=self.password)

        # Log out using a GET request which is NOT the expected method
        response = self.client.get(reverse('logout'))
        # Verify the response is 405 Method Not Allowed
        self.assertEqual(response.status_code, 405)
