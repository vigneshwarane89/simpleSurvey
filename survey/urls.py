from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path(" ",views.index,name= "root"),
    path("survey_load/", views.load_survey, name = "load-survey"),
    path(r"^survey/(?P<survey_id>\d+)/$", views.survey_view, name = "survey-detail"),



    ]
