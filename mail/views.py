from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

from .forms import MailForm,SearchForm
from.models import Mail

def home(request):
	mail_list=Mail.objects.all().order_by("-date_sent")
	return render(request,'mail/home.html',{"mail_list":mail_list})


def mail(request):
	if request.method=="POST":
		form=MailForm(request.POST)
		if form.is_valid():
			sender=form.cleaned_data["sender"]
			subject=form.cleaned_data["subject"]
			message=form.cleaned_data["message"]
			to=form.cleaned_data["to"]
			send_mail(sender,subject,message,[to])
			form.save()
			messages.success(request,"Successfully sent!")
			return redirect("home")
	else:
		form=MailForm()
	return render(request,'mail/mail.html',{"form":form})


def search(request):
	if request.method=="POST":
		form=SearchForm(request.POST)
		if form.is_valid():
			pass
	else:
		form=SearchForm()
	return render(request,'mail/results.html',{"form":form})