from django.shortcuts import render

import os

def index(request):
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