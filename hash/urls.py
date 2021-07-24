from django.urls import path
from . import views

urlpatterns = [
    # path("verify", views.verify, name = "verify"),
    # path("index", views.index, name = "index"),
    path("", views.accueil, name = "accueil")
]