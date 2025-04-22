from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "personal/about_me.html")


def ShoppingPage(request):
    return render(request, "personal/ShoppingPage.html")


def gaming_store(request):
    return render(request, "personal/gaming_store.html")
