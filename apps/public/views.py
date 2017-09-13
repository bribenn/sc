from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'public/home.html')

def demo_request(request):
	return render(request, 'public/demo_request.html')