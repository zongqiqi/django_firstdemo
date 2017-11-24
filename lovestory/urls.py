from django.conf.urls import url

from . import views

urlpatterns=[
	# url(r'^$',views.index,name='index'),
	url(r'^$',views.user_login,name='test'),
	url(r'^login$',views.login,name='login'),

	url(r'^test2/$',views.test2,name='test2'),
	url(r'^tour/$',views.tour,name='tour'),

]