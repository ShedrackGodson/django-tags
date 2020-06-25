from .views import Blog, TagIndexView
from django.urls import path

urlpatterns = [
    path('', Blog.as_view(), name='blog'),
    path('post/tags/<slug>/', TagIndexView.as_view(), name="tagged"),
]