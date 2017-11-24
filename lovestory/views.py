from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib.auth import authenticate, login 
from .forms import LoginForm
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
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,'lovestory/index.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                    return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'lovestory/login.html', {'form': form})


def test2(request):
	return render(request,'lovestory/test2.html')

def tour(request):
	return render(request,'lovestory/BaiduMap.html')