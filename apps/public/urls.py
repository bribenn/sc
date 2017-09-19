from django.conf.urls import url
from . import views           
urlpatterns = [     
	url(r'^$', views.index),
	url(r'^demo_request$', views.demo_request),
	url(r'^login$', views.login),
	url(r'^demoEmail$', views.demoEmail)
]


