from django.conf.urls import url

from . import views

urlpatterns=[
	url(r'^$',views.index),
	url(r'^(?P<namelist_id>\d+)/$',views.index,name='index'),
	url(r'^test/$',views.test,name='test'),
	url(r'^next/(?P<namelist_id>\d+)/$',views.next,name='next'),
	url(r'^before/(?P<namelist_id>\d+)/$',views.before,name='before'),
	url(r'^catalog/$',views.catalog,name='catalog'),
]	