from django.urls import path
from core import views

urlpatterns = [
    path("", views.get_all_project_urls, name="index"),
]
