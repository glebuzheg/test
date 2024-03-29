from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from image_comment.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('comment/', include('apps.comments.urls')),
    path('image/', include('apps.images.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
