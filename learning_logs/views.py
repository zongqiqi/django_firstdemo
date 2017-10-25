from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic,Entry
from .forms import TopicForm,EntryForm

from markdown import markdown

def index(request):
	"""学习笔记的主页"""
	return render(request,'learning_logs/index.html')

@login_required
def topics(request):
	"""显示所有的主题"""
	topics=Topic.objects.filter(owner=request.user).order_by('date_added')
	context={'topics':topics}
	return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
	"""显示单个主题和具体的条目信息"""
	topic=Topic.objects.get(id=topic_id)
	if topic.owner!=request.user:
		raise Http404

	entries=topic.entry_set.order_by('-date_added')
	for entry in entries:
		entry.text=markdown(entry.text,extensions=['markdown.extensions.extra',
													'markdown.extensions.codehilite',
													'markdown.extensions.toc',])


	context={'topic':topic,'entries':entries}
	return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
	if request.method!='POST':
		form=TopicForm()
	else:
		form=TopicForm(request.POST)
		if form.is_valid():
			new_topic=form.save(commit=False)
			new_topic.owner=request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
	context={'form':form}
	return render(request,'learning_logs/new_topic.html',context)

@login_required
def new_entry(request,topic_id):
	topic=Topic.objects.get(id=topic_id)
	if request.method!='POST':
		form=EntryForm()
	else:
		form=EntryForm(data=request.POST)
		if form.is_valid():
			new_entry=form.save(commit=False)
			new_entry.topic=topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
	context={'topic':topic,'form':form}
	return render(request,'learning_logs/new_entry.html',context)

@login_required
def edit_entry(request,entry_id):
	entry=Entry.objects.get(id=entry_id)
	topic=entry.topic
	if request.user!=topic.owner:
		raise Http404
	if request.method!='POST':
		form=EntryForm(instance=entry)
	else:
		form=EntryForm(instance=entry,data=request.POST)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
	context={'entry':entry,'topic':topic,'form':form}
	return render(request,'learning_logs/edit_entry.html',context)

@login_required
def search(request):
	if request.method=='POST':
		form_data=request.POST['search']
		search_result=Entry.objects.filter(text__icontains=form_data)
		entries=search_result
		for entry in entries:
			entry.text=markdown(entry.text,extensions=['markdown.extensions.extra',
													'markdown.extensions.codehilite',
													'markdown.extensions.toc',])

	# else:
	# 	from_data='No form data'
	# if request.user.username=="Zongqiqi":
	# 	msg="I am the king."
	# else:
	# 	msg=dir(request.user)
	context={'entries':entries}	
	return render(request,'learning_logs/search.html',context)