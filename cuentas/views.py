# <<<<<<< HEAD
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
# from .forms import LoginForm, UserRegistrationForm
# from django.contrib.auth.decorators import login_required


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(email=cd['email'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated')
#             else:
#                 return HttpResponse('Disabled account')
#         else:
#             return HttpResponse('Invalid Login')
#     else:
#         form = LoginForm()
#     return render(request, 'cuentas/login.html', {'form': form})


# @login_required
# def dashboard(request):
#     return render(request, 'cuentas/dashboard.html', {'section': 'dashboard'})


# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(
#                 user_form.cleaned_data['password']
#             )
#             new_user.save()
#             template = 'cuentas/register_done.html'
#             ctx = {'new_user': new_user}
#             return render(request, template, ctx)
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'cuentas/register.html', {'user_form': user_form})

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

