from django.urls import path
from .views import (
  PostListView,
  PostArchivedListView,
  PostDraftListView
)



urlpatterns = [
  path("list/", PostListView.as_view(), name="list"),
  path("archivedlist/", PostArchivedListView.as_view(), name="archived_list"),
  path("drafts/list/", PostDraftListView.as_view(), name="draft_list"),

]