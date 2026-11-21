from django.urls import path

from . import views

app_name = "articles"

urlpatterns = [
    path("", views.blogs, name="blogs"),
    path("<slug:slug>/", views.blog_details, name="blog-details"),
]
