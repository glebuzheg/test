from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from apps.images.models import Image
from .forms import CommentForm


@method_decorator(csrf_exempt, name='dispatch')
class CommentCreateView(CreateView):
    def post(self, request, *args, **kwargs):
        data = dict()
        form = CommentForm(request.POST)
        if form.is_valid():
            self.image = self._get_image(kwargs.get('image_id'))
            form.instance.image = self.image
            comment = form.save()
            data['comment'] = model_to_dict(comment)
        else:
            data['error'] = "form not valid!"
        return JsonResponse(data)

    def _get_image(self, id):
        return get_object_or_404(Image, id=id)

    def form_valid(self, form):
        self.image = get_object_or_404(Image, id=self.kwargs['image_id'])
        form.instance.image_id = self.image.id
        return super().form_valid(form)
