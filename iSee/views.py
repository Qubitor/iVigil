# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render

def base(request):
	# print "HALO"
	return render(request, 'base.html')

def train(request):
	# print "HALO"
	return render(request, 'train.html')

def test(request):
	# print "HALO"
	return render(request, 'test.html')