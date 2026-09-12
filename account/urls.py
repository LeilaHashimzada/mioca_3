from django.urls import path
from .views import auth, AccountView

urlpatterns = [
    path("auth/", auth, name="auth"),
    path("my_account/<int:pk>", AccountView.as_view(), name="my-account"),
]
