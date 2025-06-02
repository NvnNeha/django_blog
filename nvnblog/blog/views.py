from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import Post
from django.urls import reverse
from django.utils.text import slugify
from .forms import CommentModel,UserRegistrationForm,CreatePostForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def starting_page(request):
    posts = Post.objects.all().order_by("-date")[:3]
    if request.method == "POST":
        logout(request)
    return render(request, "blog/starting_page.html", {"posts": posts})


def all_posts(request):
    posts = Post.objects.all().order_by("-date")
    
    return render(request, "blog/all_posts.html", {"posts": posts})


def detailed_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    stored_list = request.session.get("stored_list")
    if stored_list is not None:
        is_save_for_later = post.id in stored_list
    else:
        is_save_for_later = False 

    comment_form = CommentModel()
    if request.method == "POST":
        comment_form = CommentModel(request.POST)
        if comment_form.is_valid():
            wait =comment_form.save(commit=False)
            wait.post = post
            wait.save()
            return HttpResponseRedirect(reverse("detailed-post", args=[slug])) 
    return render(request, "blog/detailed_post.html", {
        "post": post, 
        "comment_form": comment_form,
        "post_tag": post.tags.all(),
        "comments": post.comments.all().order_by("-id"),
        "is_save_for_later" : is_save_for_later
        })
