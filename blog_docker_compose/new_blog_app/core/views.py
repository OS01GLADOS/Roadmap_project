from django.shortcuts import render
from django.urls import URLPattern, URLResolver
from django.urls import get_resolver

# Create your views here.


def get_all_project_urls(request):
    def if_none(value):
        if value:
            return value
        return ""

    def get_all_urls(urls, parent_pattern=None):
        res = []
        for url in urls.url_patterns:
            if isinstance(url, URLResolver):
                res = res + get_all_urls(
                    url, if_none(parent_pattern) + str(url.pattern)
                )
            elif isinstance(url, URLPattern):
                res.append(str(if_none(parent_pattern) + str(url.pattern)))
        return res

    return render(
        request, "core/all_urls.html", {"url_list": get_all_urls(get_resolver())}
    )
