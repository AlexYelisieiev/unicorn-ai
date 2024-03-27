from django.urls import path
from .views import HomeView, AboutUsView, ContactsView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about_us/", AboutUsView.as_view(), name="about_us"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]
