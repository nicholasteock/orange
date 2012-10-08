#Student models

from django.db import models
from django.contrib.auuth import User
from django import forms
from django.forms import ModelForm

class Student(models.Model):
	user	= models.OneToOneField(User) #identifies student to a unique user.
	email	= models.EmailField('E-Mail', max_length = 200)
	school	= models.CharField('School', max_length = 50)
	
	def __unicode__(self):
		return self.user.username
		
class StudentForm(ModelForm):
	class Meta:
		model	= Student
		fields	=('email', 'school')