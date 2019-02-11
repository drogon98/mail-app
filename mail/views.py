from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import MailForm

def home(request):
	if request.method=="POST":
		form=MailForm(request.POST)
		if form.is_valid():
			sender=form.cleaned_data["sender"]
			subject=form.cleaned_data["subject"]
			message=form.cleaned_data["message"]
			to=form.cleaned_data["to"]
			send_mail(sender,subject,message,[to])
			form=MailForm()
	else:
		form=MailForm()
	return render(request,'mail/home.html',{"form":form})