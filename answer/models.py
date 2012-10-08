#Answer models

from django.db import models
from tutor.models import Tutor
from question.models import Question

class Answer(models.Model):
	answer		= models.ForeignKey(Question)
	content		= models.TextField()
	answered_by	= models.OneToOneField(Tutor)

	def __unicode__(self):
		return '%s' % self.content