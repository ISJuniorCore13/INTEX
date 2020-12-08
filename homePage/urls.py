from django.urls import path, include
from .views import indexPageView, addListingPageView, editListingPageView, submitAddListingPageView, removeListingPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("addjob/", addListingPageView, name="addListing"),
    path("submit", submitAddListingPageView, name="submit"),
    path("addjob/<str:edit_id>", editListingPageView, name="editListing"),
    path("removejob/", removeListingPageView, name="removeListing"),
]