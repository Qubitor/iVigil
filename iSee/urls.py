from django.conf.urls import url, include
#from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
	url(r'^iSee/$', views.base, name='iSee'),
	url(r'^accept/(\w+)/', views.accept, name="accept"),
	url(r'^reject/(\w+)/', views.reject, name="reject"),
	url(r'^popup_face_rec',views.popup_face_rec,name="popup_face_rec"),
	url(r'^demo',views.demo,name="demo"),
	url(r'^waiting_list',views.waiting_list,name="waiting_list"),

	url(r'^stream_video$',views.stream_video,name="stream_video"),

]