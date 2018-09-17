from django.conf.urls import url, include
#from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
	url(r'^iSee/$', views.base, name='iSee'),
	url(r'^train',views.train,name="train"),
	url(r'^test',views.test,name="test"),
	]