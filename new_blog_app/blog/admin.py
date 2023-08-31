from django.contrib import admin

# Register your models here.
from blog.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
