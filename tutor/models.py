from django.db import models
from django.contrib.auth import User
from django.forms import ModelForm

gender_list = (('M', 'Male'), ('F', 'Female'))

class Tutor(models.Model):
	user			= models.OneToOneField(User) #identifies tutor to a unique user in the table
	email			= models.EmailField('E-Mail', max_length = 200)
	first_name		= models.CharField('First Name', max_length = 200)
	last_name		= models.CharField('Last Name', max_length = 200)
	gender			= models.CharField('Gender', max_length = 1, choices = gender_list)
	birthday		= models.DateField('Birthday', blank = True, null = True)
	locationpref	= models.CharFieeld('Location Preferences', max_length = 200)
	phone			= models.CharField('Phone', max_length = 8)
	reject_count	= models.IntegerField('Reject count')
	qualifications	= models.CharField('Qualifications', max_length = 200, null = True)
	
	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)
	
class TutorForm(ModelForm):
	class Meta:
		model		= Tutor
		fields		= ('email', 'first_name', 'last_name', 'gender', 'birthday', 'phone', 'locationpref', 'qualifications',)
		