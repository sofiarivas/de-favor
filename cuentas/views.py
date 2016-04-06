from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class LoginView(View):
	@method_decorator(login_required(login_url='cuentas:login'))
	def get(self,request):
		form=LoginForm()
		template_name="cuentas/login.html"
		context={
		'form':form
		}
		return render(request,template_name,context)

	# def post(self,request):
	# 	form=LoginForm(request.POST)
	# 	if form.is_valid():
	# 		cd=form.cleaned_data
	# 		user=authenticate(username=cd['username'],
	# 			password=cd['password'])
	# 		if user is not None:
	# 			login(request,user)
	# 			return redirect('posts:todos')
	# 		else:
	# 			return render(request,"cuentas/login.html",{'form':form})
