from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from apps.images.forms import BaseImageForm
from .models import Image


class ImageCreateView(CreateView):
    template_name = 'image/image_create.html'
    model = Image
    form_class = BaseImageForm


class ImageDetailView(DetailView):
    template_name = 'image/image_detail.html'
    model = Image
    context_object_name = 'image'


class ImageListView(ListView):
    template_name = 'image/image_list.html'
    paginate_by = 10
    model = Image
    context_object_name = 'image_list'

    def get_queryset(self):
        return Image.objects.all()
