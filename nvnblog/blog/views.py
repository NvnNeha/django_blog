from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request, "blog/starting_page.html")

def detailed_post(request):
    return render(request, "blog/detailed_post.html")


def all_posts(request):
    return render(request,"blog/all_posts.html")