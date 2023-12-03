from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from QuizHub.models import *

def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())
