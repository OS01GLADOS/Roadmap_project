from django.shortcuts import render
from blog.models import Author
from django.views.generic import ListView


class AuthorListView(ListView):
    model = Author
    template_name = "blog/author_list_view.html"
