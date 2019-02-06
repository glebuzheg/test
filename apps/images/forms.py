from django import forms

from apps.images.models import Image


class BaseImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'name')
