from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path(
    'posts/',
    views.posts,
    name='posts'
),
    path('sobre/', views.sobre, name='sobre'), 

    path(
    'post/<slug:slug>/',
    views.post_detail,
    name='post_detail'
),
    path(
    'post/<slug:slug>/like/',
    views.like_post,
    name='like_post'
)
]