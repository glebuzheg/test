from django import forms

from apps.images.models import Image


class BaseImageForm(forms.ModelForm):
    comment = forms.CharField(max_length=32, required=False)

    class Meta:
        model = Image
        fields = ('image', 'comment')
