from django.conf.urls import patterns, url
from crowdsourcing import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^task/(?P<task_name_slug>[\w\-]+)/$', views.task, name='task'),
)