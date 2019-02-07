from django.urls import path

from .views import CommentCreateView

urlpatterns = [
    path('<int:image_id>/create/', CommentCreateView.as_view(), name='comment_create'),

]
