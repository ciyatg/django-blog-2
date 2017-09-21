#The first version of this code is copied from posts app's urls.py.
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from i_was_here.models import was_here

urlpatterns = [ url(r'^$', ListView.as_view(
                                    queryset=was_here.objects.all(),
                                    template_name="i_was_here/posts.html")),
                
                ]
