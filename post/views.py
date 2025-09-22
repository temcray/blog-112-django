from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView
    
)

from .models import Post
from django.contrib.auth.models import User


# Create your views here.
class PostListView(ListView):
  model = Post
  template_name = "posts/list.html"


class PostDetailView(DetailView):
  model = Post
  template_name = "posts/detail.html"


class PostCreateView(CreateView):
  model = Post 
  template_name = "posts/new.html"
  fields = ["title", "content"]

  class PostDeleteView(DeleteView):
    model = Post 
    template_name = "posts/delete.html"
    success_url = reverse_lazy("post_list")

