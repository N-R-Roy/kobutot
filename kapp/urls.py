from django.urls import path
from . import views

app_name = "kapp"

urlpatterns = [
    path("", views.login, name="login"),
    path("login_handler/", views.login_handler, name="login_handler"),
    path("home/<str:user_id>/", views.home, name="home"),
    path("registration/", views.registration, name="registration"),
    path("registration_handler/", views.registration_handler, name="registration_handler"),
]


