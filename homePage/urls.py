from django.urls import path, include
from .views import indexPageView, addListingPageView, editListingPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("addjob/", addListingPageView, name="addListing"),
    path("addjob/<str:edit_id>", editListingPageView, name="addListing")
]