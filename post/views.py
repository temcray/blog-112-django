from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    
    
)

from .models import Post, Status
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    
)

# Create your views here.
class PostListView(ListView):
  template_name = "post/list.html"
  #model = Post
  context_object_name = "post_list"
  status = Status.objects.get(name="published")
  queryset = Post.objects.filter(status=status).order_by("created_on").reverse()


  def get_context_data(self, **kwargs):
    context = super() .get_context_data(**kwargs)
    print(context)
    return context
    
    
    

class PostDraftListView(LoginRequiredMixin, ListView):
  template_name = "post/draft_list.html"
  context_object_name = "drafts"
  status = Status.objects.get(name="drafts")
  queryset = Post.objects.filter(status=status).order_by("created_on").reverse()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    draft_post = context['drafts'].filter(author=self.request.user)
    context['drafts'] = draft_post
    return context
    
    


class PostArchivedListView(LoginRequiredMixin, ListView):
  template_name = "post/archived_list.html"
  context_object_name = "archived"
  status = Status.objects.get(name="archived")
  queryset = Post.objects.filter(status=status).order_by("created_on").reverse()

  def get_context_data(self, **kwargs):
    context = super() .get_context_data(**kwargs)
    archived_post = context['archived'].filter(author=self.request.user)
    context['archived_post'] = archived_post
    return context
    
    


class PostCreatePostView(LoginRequiredMixin, CreateView):
  template_name = "post/new.html"
  model = Post
  fields = ['title', 'subtitle', 'body', 'status']

  def form_vaild(self,form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
  
  

  class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = "post/detail.html"
    model = Post
    

class PostDeleteView(DeleteView):
  template_name = "post/delete.html"
  model = Post
  success_url = reverse_lazy("list")


class PostUpdateView(UpdateView):
  template_name = "post/edit.html"
  model = Post
  fields = ["title", "subtitle", "body", "status"]

  def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

  def get_success_url(self):
    return reverse_lazy("details", kwargs={"pk": self.object.pk})


