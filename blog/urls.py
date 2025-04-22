from django.urls import path
from . import views    # this is going to import all the functions from views file

app_name = 'blog'

urlpatterns = [
    path("", views.blog_list, name='blog_list'),
    path('<int:post_id>/', views.blog_detail, name='blog_detail')
]
