from django.urls import path

from apps.images.views import ImageCreateView, ImageDetailView, ImageListView, CommentListView

urlpatterns = [
    path('list/', ImageListView.as_view(), name='image_list'),
    path('create/', ImageCreateView.as_view(), name='image_create'),
    path('detail/<int:image_id>', ImageDetailView.as_view(), name='image_detail'),
    path('<int:image_id>/comments/', CommentListView.as_view(), name='comment_list'),
]
