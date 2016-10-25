from django.conf.urls.static import static

from BlogEngine import settings

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
