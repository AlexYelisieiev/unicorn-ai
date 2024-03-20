from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser


class ResumeCreateViewTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='user', password='password')
    
    def test_resume_create_view_template(self):
        self.client.login(username='user', password='password')
        response = self.client.get(reverse("resume_create", args=["user"]))
        self.assertContains(response, "Create resume")

