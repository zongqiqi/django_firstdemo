from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse

from .models import NameList


# file_path='E:\\zongqiqi\\biandaima\\mypython\\txtread\\'
# filename='index.txt'
# with open(file_path+filename) as file:
# 	lines=file.readlines()
	

def index(request,namelist_id=1):
	# path="E:\\zongqiqi\\biandaima\\mypython\\txtread\\第一章.txt"
	filepath="E:\\zongqiqi\\biandaima\\mypython\\txtread\\"
	a=NameList.objects.get(id=namelist_id)
	# with open(filepath+a.name+'.txt') as file:
	# 	text=file.read()
	namelist=[]
	for i in range(12):
		if int(namelist_id)-5+i <0:
			namelist=NameList.objects.all()[:12]
			break
		if int(namelist_id)-5+i >len(namelist):
			namelist=NameList.objects.all()[772:]
			break
		else:
			namelist.append(NameList.objects.get(id=str(int(namelist_id)-5+i)))
	context={'a':a,'namelist':namelist,'namelist_id':namelist_id}
	return render(request,'reading/index.html',context)

#just test don't care
def test(request):
	return render(request,'reading/test.html')

#上一页
def next(request,namelist_id):
	newnamelist_id=int(namelist_id)+1
	return HttpResponseRedirect(reverse('reading:index',args=[newnamelist_id]))
#上一页
def before(request,namelist_id):
	newnamelist_id=int(namelist_id)-1
	return HttpResponseRedirect(reverse('reading:index',args=[newnamelist_id]))

#还差一个目录
def catalog(request):
	alllist=NameList.objects.all()
	alllist_1=alllist[:200]
	alllist_2=alllist[200:400]
	alllist_3=alllist[400:600]
	alllist_4=alllist[600:]
	context={'alllist_1':alllist_1,'alllist_2':alllist_2,'alllist_3':alllist_3,'alllist_4':alllist_4,}
	return render(request,'reading/catalog.html',context)