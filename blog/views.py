from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_list_page.html', {"posts": posts})


@login_required
def blog_detail(request, post_id):
    # This will pull the object from the db with the id 
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'blog/blog_detail_page.html', { "post": post})