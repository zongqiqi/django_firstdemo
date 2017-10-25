from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,Http404

import os

# def index(request):
# 	images=[]
# 	path=r'/static/lovestory/loveimage/'
# 	pwd=os.path.dirname(__file__)
# 	dest=pwd+path
# 	files=os.listdir(dest)
# 	for file in files:
# 		mijp=os.path.splitext(file)[1]
# 		if mijp=='.jpg':
# 			file2='lovestory/loveimage/'+file
# 			images.append(file2)
# 	context={'images':images}
# 	return render(request,'lovestory/index.html',context)

def test(request):
	return render(request,'lovestory/login.html')
	# if request.GET['username'] in ['zongqiqi','wangxiao'] and request.GET['password'] in ['xy0522']:
	# 	return HttpResponseRedirect(reverse('love:index',))
def login(request):
	if request.GET['username'] in ['zongqiqi','wangxiao'] and request.GET['password'] in ['xy0522']:
		# return HttpResponseRedirect(reverse('love:index',))
		images=[]
		path=r'/static/lovestory/loveimage/'
		pwd=os.path.dirname(__file__)
		dest=pwd+path
		files=os.listdir(dest)
		for file in files:
			mijp=os.path.splitext(file)[1]
			if mijp=='.jpg':
				file2='lovestory/loveimage/'+file
				images.append(file2)
		context={'images':images}
		return render(request,'lovestory/index.html',context)
	else:
		raise Http404


def test2(request):
	return render(request,'lovestory/test2.html')