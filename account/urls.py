from django.urls import path
from .views import login, account

urlpatterns = [
    path("login/", login, name="login"),
    path("my-account/", account, name="my-account"),
]
