from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from . import forms
from forms import DemoForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index(request):
	return render(request, 'public/home.html')

def demo_request(request):
	return render(request, 'public/demo_request.html')

def login(request):
	if request.method == 'POST':
		password = "ShieldBank2017"
		here = request.POST.get('next')

		if request.POST.get('password') == password:
			request.session['logged_in'] = 'true'
			return render(request, 'private/home_2.html')

		messages.add_message(request, messages.INFO, "sorry, wrong password", extra_tags="login")
	return redirect(request, here)

def demoEmail(request):
	name = request.POST.get('name', '')
	company = request.POST.get('company', '')
	email = request.POST.get('email', '')
	phone = request.POST.get('phone', '')
	interest = request.POST.get('interest', '')