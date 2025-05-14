from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BlogListView(TemplateView):
    template_name = 'blog_list.html'