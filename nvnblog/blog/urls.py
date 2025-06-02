from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts/", views.all_posts, name="all-posts"),
    path("posts/<slug:slug>", views.detailed_post, name="detailed-post"),
    path("stored-posts/", views.stored_posts, name="stored-posts"),
    path("create-post/", views.create_post, name="create-post"),
    path("edit-post/<slug:slug>/", views.edit_post, name="edit-post"),
    path("delete-post/<slug:slug>/", views.delete_post, name="delete-post"),
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login")

]