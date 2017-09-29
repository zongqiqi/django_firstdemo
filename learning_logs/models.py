from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	"""用户学习的主题"""
	owner=models.ForeignKey(User)
	text=models.CharField(max_length=200)
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""返回模型的字符串表示"""
		return self.text

class Entry(models.Model):
	"""条目：学到关于某个主题的具体知识"""
	topic=models.ForeignKey(Topic)
	name=models.CharField(max_length=200,default="None")
	text=models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural='entries'

	def __str__(self):
		return self.text[0:50]+"..."