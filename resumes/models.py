from audioop import reverse
from django.db import models
from accounts.models import CustomUser


# Create your models here.
class Resume(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    job_title = models.TextField(default="", null=False, blank=False)
    skills = models.TextField(default="", null=False, blank=False)
    languages = models.TextField(default="", null=False, blank=False)
    about = models.TextField(default="", null=False, blank=False)
    experience = models.TextField(default="", null=False, blank=False)
    let_anon_users_see_resume = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.job_title

    def get_absolute_url(self) -> str:
        return reverse("resume_detail", kwargs={"username": self.owner})
