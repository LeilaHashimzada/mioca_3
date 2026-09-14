from django.urls import path
from .views import auth_view, AccountView

urlpatterns = [
    path("auth/", auth_view, name="auth"),
    path("my_account/<int:pk>", AccountView.as_view(), name="my-account"),
]