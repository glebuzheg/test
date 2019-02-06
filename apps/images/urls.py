from django.urls import path

from apps.images.views import ImageCreateView, ImageDetailView, ImageListView

urlpatterns = [
    path('list/', ImageListView.as_view(), name='image_list'),
    path('create/', ImageCreateView.as_view(), name='image_create'),
    path('detail/<int:pk>', ImageDetailView.as_view(), name='image_detail'),

]
