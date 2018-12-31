from django.conf.urls import url, include
#from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
	url(r'^sample/$', views.base, name='sample'),
	url(r'^accept/(\w+)/', views.accept, name="accept"),
	url(r'^reject/(\w+)/', views.reject, name="reject"),
	url(r'^waiting_list',views.waiting_list,name="waiting_list"),
	url(r'^delete',views.delete,name="delete"),
	url(r'^create',views.create,name="create"),
	url(r'^clear',views.clear,name="clear"),
	url(r'^add',views.add,name="add"),
	url(r'^cut',views.cut,name="cut"),
	url(r'^generate',views.generate,name="generate"),
	url(r'^stream_video$',views.stream_video,name="stream_video"),
	url(r'^accept_list',views.accept_list,name="accept_list"),
	url(r'^reject_list',views.reject_list,name="reject_list"),
	url(r'^notifi_data',views.notifi_data,name="notifi_data"),
	url(r'^accept_api',views.accept_api,name="accept_api"),
	url(r'^rej_api',views.rej_api,name="rej_api"),
	# url(r'^review',views.review,name="review"),
	url(r'^sam',views.sam,name="sam"),
	url(r'^test',views.test,name="test"),
	url(r'^rev',views.rev,name="rev"),

]