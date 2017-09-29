from django.shortcuts import render



def index(request):
	"""BACKGRAND背景"""
	return render(request,'mytest/index.html')
