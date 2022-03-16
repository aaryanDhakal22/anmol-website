from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.blogView, name="blog"),
    path("staff/", views.staffView, name="staff"),
    path("new", views.createBlog, name="new"),
]
