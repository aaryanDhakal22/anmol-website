from django.shortcuts import redirect, render

# Create your views here.


def blogView(request):
    return render(request, "blogs.html")


def createBlog(request):
    context = {}
    if request.method == "POST":
        context = {
            "title": request.POST["title_text"],
            "body": request.POST["body_text"],
        }

    return render(request, "blogs.html", context)
