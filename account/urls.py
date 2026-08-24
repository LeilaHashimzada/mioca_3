from django.urls import path
from .views import auth, account

urlpatterns = [
    path("auth/", auth, name="auth"),
    path("my_account/", account, name="my-account"),
]
