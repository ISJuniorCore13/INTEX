from django.urls import path, include
from .views import indexPageView, searchPageView, jobPostView, externalAppSurveyView, surveySubmitView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("search/", searchPageView, name="search"),
    path("post/<str:job_title>/<int:jobListing_id>/", jobPostView, name="post"),
    path("externalAppSurvey/", externalAppSurveyView, name="externalsurvey"),
    path("externalAppSurvey/survey/", surveySubmitView, name="survey"),
]