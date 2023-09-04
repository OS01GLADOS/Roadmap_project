from django.shortcuts import render, redirect
from blog.models import Author
from django.views.generic import ListView
from django.contrib.auth import login, authenticate, logout
from blog.forms import SignupForm, PostCreateForm, LoginForm
from django.contrib.auth.decorators import login_required


class AuthorListView(ListView):
    model = Author
    template_name = "blog/author_list_view.html"


# register view
def signup_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("blog:authors")

        form = SignupForm()
        return render(request, "blog/signup.html", {"form": form})
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("blog:authors")
    else:
        form = SignupForm()
    return render(request, "blog/signup.html", {"form": form})


def login_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("blog:authors")

        form = LoginForm()
        return render(request, "blog/login.html", {"form": form})

    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("blog:authors")

        # either form not valid or user is not authenticated
        return render(request, "blog/login.html", {"form": form})


def logout_view(request):
    username = request.user.username
    if username is not None:
        logout(request)
        return redirect("index")


@login_required(login_url="/blog/login")
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()

            return redirect("blog:authors")
    form = PostCreateForm()
    return render(request, "blog/post_create.html", {"form": form})
