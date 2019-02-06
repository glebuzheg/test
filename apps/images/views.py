from django.http import HttpResponseRedirect
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

    def form_valid(self, form):
        instance = self.object = form.save()
        if form.cleaned_data.get('comment'):
            comm = instance.comments.create(text=form.cleaned_data['comment'])
            comm.save()
        return HttpResponseRedirect(reverse('image_list'))


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
