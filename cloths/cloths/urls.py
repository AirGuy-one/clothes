from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cloths import settings
from store.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('reg_app/', include('reg.urls')),
    path('api/', include('drf_api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound




