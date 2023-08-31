from django.urls import path
from blog import views


app_name = "blog"
urlpatterns = [
    path("authors", views.AuthorListView.as_view(), name="authors"),
]
