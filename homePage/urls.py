from django.urls import path, include
from .views import indexPageView, addListingPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("addjob/", addListingPageView, name="addListing")
]