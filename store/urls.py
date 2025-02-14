from django.urls import path
from .views import store, login_view


urlpatterns = [
    path("", store, name="store"),
    path("login/", login_view, name="login")
]