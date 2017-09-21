from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from . import forms
from forms import DemoForm
from django.core.mail import send_mail, BadHeaderError


# Create your views here.
def index(request):
	request.session['logged_in'] = False
	return render(request, 'public/home.html')

def demo_request(request):
	return render(request, 'public/demo_request.html')

def login(request):
	if request.method == 'POST':
		password = "ShieldBank2017"
		here = request.POST.get('here')

		if request.POST.get('password') == password:
			request.session['logged_in'] = True
			# return render(request, 'private/home_2.html')
			return JsonResponse({'logged_in':True})

		# messages.add_message(request, messages.INFO, "sorry, wrong password", extra_tags="login")
	# return redirect(here)
	return JsonResponse({
		'error': {
			'message': "Sorry, wrong password.",
			'form': 'login'
		}
	})

