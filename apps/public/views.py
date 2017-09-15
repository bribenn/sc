from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	if request.method != 'POST':
		return redirect('/')
	#validate password
	password = "ShieldBank2017"
	if request.POST.get('password') == password:
		request.session['user_id'] = user.id
		return redirect('/user_profile')
	else: 
		messages.add_message(request, messages.INFO, 'invalid credentials', extra_tags="login")
		return redirect('/')
	return render(request, 'public/home.html')

def demo_request(request):
	return render(request, 'public/demo_request.html')