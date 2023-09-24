from django.urls import path

from . import views
from .views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.RegisterPageView.as_view(), name="register"),
    path("transactions/", views.transactions, name="transactions"),
    path("transactions/add/", views.add_transaction, name="add_transaction"),
]
