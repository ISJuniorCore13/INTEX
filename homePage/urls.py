from django.urls import path, include
from .views import indexPageView, addListingPageView, editListingPageView, submitAddListingPageView, removeListingPageView, updateListingPageView, userProfilePageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("addjob/", addListingPageView, name="addListing"),
    path("submit", submitAddListingPageView, name="submit"),
    path("update", updateListingPageView, name="update"),
    path("addjob/<str:edit_id>", editListingPageView, name="editListing"),
    path("removejob/", removeListingPageView, name="removeListing"),
    path("profile/<str:user_id>", userProfilePageView, name='profile')
]