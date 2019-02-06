from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from image_comment.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('comments/', include('apps.comments.urls')),
    path('images/', include('apps.images.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
