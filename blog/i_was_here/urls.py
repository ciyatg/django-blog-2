from django.conf.urls import url
from . import views

urlpatterns = [ url(r'^$', views.here_list, name='here_list'),
                url(r'^post/new/$', views.post_new, name='post_new'),
                ]
