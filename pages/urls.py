from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path("about-us/", AboutPageView.as_view(), name="about"),
]
