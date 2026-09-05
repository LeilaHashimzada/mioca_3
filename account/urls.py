from django.urls import path
from .views import auth_view, account

urlpatterns = [
    path("login/", auth_view, name="login"),
    path("my-account/", account, name="my-account"),
]