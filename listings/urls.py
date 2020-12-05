from django.urls import path, include
from .views import indexPageView, searchPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("search/", searchPageView, name="search"),
]