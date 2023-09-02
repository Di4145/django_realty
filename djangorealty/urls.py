from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from realtys.views import index, search
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('search/', search, name='search_page'),
    # path('detail/', detail, name='detail_search')
]



if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)