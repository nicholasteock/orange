#Tutor views

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from tutor.models import Tutor
from django.contrib.auth.decorators import login_required

@login_required
def show_topics(request):
	#return HttpResponseRedirect('/topiclist/')
	
def show_
	