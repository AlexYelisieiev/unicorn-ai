from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    def test_home_view_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Welcome to Unicorn AI!")
        self.assertContains(response, "Log in")
        self.assertContains(response, "Sign up")
    
    def test_home_view_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Welcome to Unicorn AI!")
