from django.urls import path
from blog import views


app_name = "blog"
urlpatterns = [
    path("authors", views.AuthorListView.as_view(), name="authors"),
    path("register", views.signup_view, name="signup"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("post-create", views.post_create, name="create_post"),
]
