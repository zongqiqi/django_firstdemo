from django.contrib import admin

from .models import Topic,Entry

class EntryAdmin(admin.ModelAdmin):
	list_display=('id','topic','name','date_added')#设置在管理对象列表中显示的字段
	list_filter=('topic','text','date_added')#右侧边栏根据list_filter属性中指定的字段返回结果
	search_fields=('text',)#定义一个搜索字段列

	ordering=['id']#默认排序方式







admin.site.register(Topic)
admin.site.register(Entry,EntryAdmin)
