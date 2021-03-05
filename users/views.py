from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

def register(request):
	if request.method == "POST":
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'An account has been created for {username}!')
			return redirect('register')
	else: 
		form = UserRegistrationForm()
		context = {'form': form}
		return render(request, 'users/register.html',context)


