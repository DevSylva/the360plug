from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .models import *

# Create your views here.

def index(request):
    context = {'business':business}
    return render(request, 'index.html', context)

def about(request):
	context = {'business':business}
	return render(request, 'services.html', context)

business = Business.objects.all()
def services(request):
    context = {'business' : business}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def sent(request):
	messageObj = Message()

	name = request.POST.get('name')
	email = request.POST.get('email')
	phonenumber = request.POST.get('phonenumber')
	msg = request.POST.get('msg')

	messageObj.name = name
	messageObj.emailAddress = email
	messageObj.phoneNumber = phonenumber
	messageObj.message = msg
	messageObj.save()

	context = {'business':business}
	return render(request, 'message_sent.html', context)


