from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser


class SignUpViewTest(TestCase):
    def test_signup_view_contains_signup_button(self):
        response = self.client.get(reverse("signup"))
        self.assertContains(response, "Sign up")

    def test_login_view_contains_login_button(self):
        response = self.client.get(reverse("login"))
        self.assertContains(response, "Log in")
    
    def test_signup_view_contains_login_button(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Log in")
    

