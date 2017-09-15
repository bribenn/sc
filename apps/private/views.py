from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def home_2(request):
	return render(request, 'private/home_2.html')

def features(request):
	return render(request, 'private/features.html')

def expertise(request):
	return render(request, 'private/expertise.html')

def partner(request):
	return render(request, 'private/partner.html')

def about(request):
	return render(request, 'private/about.html')

def logout(request):
	print request.method
	return render(request, 'public/home.html')