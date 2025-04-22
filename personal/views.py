from django.shortcuts import render

"""
This module contains the views for the personal application.
The views handle rendering different pages like the about me page, shopping page, and gaming store page.
"""

def index(request):
    """
    View function to render the 'about_me' page.
    
    This function renders the 'personal/about_me.html' template when accessed.
    """
    return render(request, "personal/about_me.html")


def ShoppingPage(request):
    """
    View function to render the shopping page.
    
    This function renders the 'personal/ShoppingPage.html' template, which likely displays items 
    available for shopping or some related content.
    """
    return render(request, "personal/ShoppingPage.html")


def gaming_store(request):
    """
    View function to render the gaming store page.
    
    This function renders the 'personal/gaming_store.html' template, which likely showcases 
    products related to gaming, such as video games, consoles, or accessories.
    """
    return render(request, "personal/gaming_store.html")
