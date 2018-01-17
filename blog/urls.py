from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    url(r'^$',index,name='index'),
    #url(r'^delete/(\d+)/$',delete, name='delete'),
    url(r'^delajax/$',delajax, name='delajax'),
    url(r'^search/$',search, name='search'),
] + static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)