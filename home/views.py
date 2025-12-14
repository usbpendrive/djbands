from django.http import HttpResponse
from django.shortcuts import render


def credits(request):
    content = {"Nicky\nYour Name"}

    return HttpResponse(content, content_type="text/plain")

def news(request):
    data = {
        'news': [
            "DJBand now has a news page!",
            "DJBand has its first web page",
        ]
    }

    return render(request, "news.xhtml", data)
