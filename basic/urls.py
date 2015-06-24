from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.landing, name='landing'),
    url(r'^signup/test/1/$', views.test)
]
