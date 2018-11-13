from django.conf.urls import url, include
#from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
	url(r'^iSee/$', views.base, name='iSee'),
	url(r'^accept/(\w+)/', views.accept, name="accept"),
	url(r'^reject/(\w+)/', views.reject, name="reject"),
	url(r'^demo',views.demo,name="demo"),
	url(r'^waiting_list',views.waiting_list,name="waiting_list"),

	url(r'^stream_video$',views.stream_video,name="stream_video"),
	# url(r'^get_data',views.get_data,name="get_data"),
	url(r'^notifi_data',views.notifi_data,name="notifi_data"),


]
