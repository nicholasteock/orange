#Question models

from django.db import models
from student.models import Student

class Question(models.Model):
	class Meta:
		ordering	= ['pub_date']
	topic		= models.ForeignKey(Topic)
	content		= models.TextField()
	student		= models.ForeignKey(Student)
	pub_date	= models.DateTimeField(auto_now_add = True)
	
	def __unicode__ (self):
		return '%s' % self.subject.name
		
