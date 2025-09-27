from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    
    
)

from .models import Post, Status


# Create your views here.
class PostListView(ListView):
  template_name = "post/list.html"
  model = Post
  context_object_name = "post_list"
  status = Status.objects.get(name="published")
  queryset = Post.objects.filter(status=status).order_by("created_on").reverse()


  def get_context_data(self, **kwargs):
    context = super() .get_context_data(**kwargs)
    print(context)
    return context
    

  class PostDraftListView(ListView):
      template_name = "post/drafts"
      status = Status.objects.get(name="draft")
      queryset = Post.objects.filter(status=status).order_by("created_on").reverse()


  class PostArchivedListView(ListView):
      template_name = "post/archived_list.html"
      context_object_name = "archived"
      status = Status.objects.get(name="archived")
      queryset = Post.objects.filter(status=status).order_by("created_on").reverse()





