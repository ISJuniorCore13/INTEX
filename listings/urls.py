from django.urls import path, include
from .views import indexPageView, searchPageView, jobPostView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("search/", searchPageView, name="search"),
    path("post/<str:job_title>/<int:jobListing_id>/", jobPostView, name="post")
]