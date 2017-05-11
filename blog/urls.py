from django.conf.urls import url
from django.views.generic import TemplateView

from blog import views

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail, name='post_detail'),
    url(r'^translations/$', TemplateView.as_view(template_name='post/translations.html')),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
]
