from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, ListView

from apps.images.models import Image
from .models import Comment
from .forms import CommentForm


class CommentCreateView(CreateView):
    template_name = 'comments/comment_create.html'
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('image_list')

    def get_context_data(self, **kwargs):
        self.image = get_object_or_404(Image, id=self.kwargs['image_id'])
        kwargs['image'] = self.image
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.image = get_object_or_404(Image, id=self.kwargs['image_id'])
        form.instance.image = self.image
        return super().form_valid(form)


class CommentListView(ListView):
    pass
