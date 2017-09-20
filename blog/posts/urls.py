from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from posts.models import Post

urlpatterns = [ url(r'^$', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:20],
                                    template_name="posts/posts.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view( #pk means primary key, \d means digit, + means "one or more", \d+ meeans one or more digits.
                                    model = Post,
                                    template_name="posts/post.html")),
                ]
