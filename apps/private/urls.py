from django.conf.urls import url
from . import views 

urlpatterns = [ 
	url(r'^home_2$', views.home_2),
	url(r'^features$', views.features),
	url(r'^expertise$', views.expertise), 
	url(r'^partner$', views.partner),
	url(r'^about$', views.about)   
]