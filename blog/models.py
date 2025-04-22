from django.db import models

"""
This module contains the Post model, which is used to represent blog posts or similar content in the application.
The Post model includes fields for the title, signature, body, and date of the post.
Each field serves a specific purpose to store key information about a post, and the model includes a method for returning a string representation of the post.
"""

class Post(models.Model):
    """
    A model that represents a blog post or similar content.
    Stores the title, signature, body, and date of the post.
    
    Fields:
        - title: A short title for the post (max length 140 characters).
        - signature: A brief description or subtitle for the post (max length 200 characters).
        - body: The main content of the post, which can be longer text.
        - date: The publication date of the post.

    Methods:
        __str__: Returns the title of the post as a string representation.
    """
    title = models.CharField(max_length=140)
    signature = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        """
        String representation of the Post model.
        
        Returns:
            str: The title of the post.
        
        This method is useful for displaying a concise representation of the post, typically used 
        in Django admin or when referring to the object in the Django shell.
        """
        return self.title
