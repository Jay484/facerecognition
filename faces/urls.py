from django.urls import path
from django.conf import urls
from . import views

urlpatterns = [
    urls.url(r'',views.index,name='name'),
    path('', views.index, name='index'),
]