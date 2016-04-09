from django.shortcuts import render, redirect
from .forms import ContactForm
from django.template.loader import get_template
from django.template import Context
from main import urls
from django.views.generic import View
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect


class ContactoView(View):
	def get(self,request):
		template_name="contacto.html"
		form=ContactForm()
		context={
		'form':form,
		}
		return render(request, template_name,context)

	def post(self, request):
		form=ContactForm(request.POST)	
		if form.is_valid():
			subject = form.cleaned_data['subject']
			contact_name = request.POST.get('contact_name', 'contact_name')
			contact_email = request.POST.get('contact_email', 'contact_email')
			content = request.POST.get('content', 'content')
			template = get_template('contact_template.txt')
			context = Context({
			'contact_name': contact_name,
			'contact_email': contact_email,
			'content': content,
			})
			content = template.render(context)

			email = EmailMessage(
			"Nuevo mensaje",
			content,
			"defavor.com" +'',
			['defavorcontacto@gmail.com'],
			headers = {'Reply-To': contact_email }
			)
			email.send()
			# return redirect ('')

			return render(request, 'contacto.html', {
				'form': form,
			    })
			
		else:
				return render(request,"",{'form':form})




