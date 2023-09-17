from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from realtys.views import index, search, detail, contacts
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index_page'),
    path('search/', search, name='search_page'),
    path('detail/<int:id>/', detail, name='detail_page'),
    path('contacts/', contacts, name='contacts_page')
]



if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)