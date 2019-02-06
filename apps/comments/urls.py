from django.urls import path

from .views import CommentListView, CommentCreateView

urlpatterns = [
    path('<int:image_id>/create/', CommentCreateView.as_view(), name='comment_create'),
    path('list/', CommentListView.as_view(), name='comment_list'),
]
