from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("verify_email", views.verify_email, name="verify_email"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
]