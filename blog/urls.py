from django.urls import path
from .views import BlogView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView
urlpatterns = [
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
    path("<int:pk>/edit/", BlogUpdateView.as_view(), name="blog_edit"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("", BlogView.as_view(), name="blog")
]