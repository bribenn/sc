from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def home_2(request):
	if request.session['logged_in'] == True:
		return render(request, 'private/home_2.html')
	else:
		return redirect('/')

def features(request):
	if request.session['logged_in'] == True:
		return render(request, 'private/features.html')
	else:
		return redirect('/')

def expertise(request):
	if request.session['logged_in'] == True:
		return render(request, 'private/expertise.html')
	else:
		return redirect('/')

def partner(request):
	if request.session['logged_in'] == True:
		return render(request, 'private/partner.html')
	else:
		return redirect('/')

def about(request):
	if request.session['logged_in'] == True:
		return render(request, 'private/about.html')
	else:
		return redirect('/')

def logout(request):
	print "logged out"
	request.session['logged_in'] == False
	print "session", request.session
	return redirect("/")