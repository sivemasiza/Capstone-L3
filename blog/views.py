from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required

"""
This module contains the views for the blog application.
The views allow authenticated users to see a list of all posts and view individual post details.
"""

@login_required
def blog_list(request):
    """
    View function to display a list of all blog posts.
    This view is only accessible to authenticated users.
    
    Retrieves all the posts from the database and renders them on the 'blog_list_page.html' template.
    """
    posts = Post.objects.all()
    return render(request, 'blog/blog_list_page.html', {"posts": posts})


@login_required
def blog_detail(request, post_id):
    """
    View function to display the details of a specific blog post.
    This view is only accessible to authenticated users.

    Retrieves a specific post based on the provided post_id. If the post does not exist, 
    it raises a 404 error. The post is then rendered on the 'blog_detail_page.html' template.
    
    Args:
        post_id (int): The ID of the post to be displayed.
    """
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/blog_detail_page.html', {"post": post})
