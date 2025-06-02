from django.urls import path
from . import views
urlpatterns= [
    path("", views.starting_page, name="starting-page"),
    path("post", views.all_posts, name="all-posts"),
    path("post/<slug:slug>", views.detailed_post, name="detailed-post"),

]