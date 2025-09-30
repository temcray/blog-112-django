from django.urls import path
from .views import (
  PostListView,
  PostArchivedListView,
  PostDraftListView,
  PostCreatePostView,
  PostDetailView,
  PostDeleteView,
  PostUpdateView
)



urlpatterns = [
  path("list/", PostListView.as_view(), name="list"),
  path("archivedlist/", PostArchivedListView.as_view(), name="archived_list"),
  path("drafts/list/", PostDraftListView.as_view(), name="draft_list"),
  path("new/", PostCreatePostView.as_view(), name="new"),
  path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
  path("<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
  path("<int:pk>/edit/", PostUpdateView.as_view(), name="post_update"),

]