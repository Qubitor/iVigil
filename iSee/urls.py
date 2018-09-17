from django.conf.urls import url, include
#from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
	url(r'^iSee/$', views.base, name='iSee'),
	url(r'^train',views.train,name="train"),
	url(r'^test',views.test,name="test"),
	url(r'^popup_face_rec',views.popup_face_rec,name="popup_face_rec"),
	]