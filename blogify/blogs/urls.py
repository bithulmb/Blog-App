
from django.urls import path,include
from .views import BlogListView


urlpatterns = [
    path('blogs',BlogListView.as_view(),name='blog-list')
    
   
]
