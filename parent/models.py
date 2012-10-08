#Parent models

from django.db import models
from django.contrib.auth import User

salut_list	= (('Mr', 'Mr'), ('Mrs', 'Mrs'))

class Parent(models.Model):
	user		= models.OneToOneField(User)	#identifies parent to a unique user
	email		= models.EmailField('E-Mail', max_length = 200)
	salutation	= models.CharField('Salutation', max_length = 3, choices = salut_list)
	first_name	= models.CharField('First Name', max_length = 200)
	last_name	= models.CharField('Last Name', max_length = 200)
	address		= models.CharField('Address', max_length = 200)
	phone		= models.CharField('Phone', max_length = 8)
	
	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)
		
class ParentForm(ModelForm):
	class Meta:
		model	= Parent
		fields	= ('email', 'salutation', 'first_name', 'last_name', 'address', 'phone')
		
		def clean_phone(self):
			phone = self.cleaned_data.get('phone')
			if not phone.isdigit:
				raise forms.ValidationError("Telephone number only has digits!")
			return phone