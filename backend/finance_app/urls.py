from django.urls import path

from . import views
from .views import HomePageView

urlpatterns = [
    # path("", views.index, name="index"),
    path("", HomePageView.as_view(), name="home"),
    path("transactions/", views.transactions, name="transactions"),
    path("transactions/add/", views.add_transaction, name="add_transaction"),
]
