#The first version of this code is copied from posts app's urls.py.
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from i_was_here.models import was_here

urlpatterns = [ url(r'^$', ListView.as_view(
                                    queryset=was_here.objects.all().order_by("-date")[:20],
                                    template_name="posts/posts.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view( #pk means primary key, \d means digit, + means "one or more", \d+ meeans one or more digits.
                                    model = was_here,
                                    template_name="posts/post.html")),
                ]
