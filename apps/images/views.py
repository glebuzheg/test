from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.base import View

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
    pk_url_kwarg = 'image_id'


class ImageListView(ListView):
    template_name = 'image/image_list.html'
    paginate_by = 10
    model = Image
    context_object_name = 'image_list'

    def get_queryset(self):
        return Image.objects.all()


class CommentListView(View):
    image_lookup = 'image_id'

    _image = None

    def get(self, request, *args, **kwargs):
        json_comment_list = []
        image = self._get_image()

        for comment in image.comments.all():
            json_comment_list.append({
                'text': comment.text
            })

        return JsonResponse({'comments': json_comment_list})

    def _get_image(self):
        image_pk = self.kwargs.get(self.image_lookup)
        return get_object_or_404(Image, pk=image_pk)
