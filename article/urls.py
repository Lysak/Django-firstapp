from django.conf.urls import url


from article.views import *

urlpatterns = [
    url(r'^1/', basic_one),
    url(r'^2/', template_two),
    url(r'^3/', template_three_simple),
    url(r'^articles/all/$', articles),
    url(r'^articles/get/(?P<article_id>\d+)/$', article),
    url(r'^articles/addlike/(?P<article_id>\d+)/$', addlike),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', addcomment),
    url(r'^$', articles)
]
