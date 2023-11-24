from django.contrib import admin


from blog.models import Author, Post


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
