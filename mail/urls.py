from django.urls import path

from mail import views

urlpatterns=[
   path('home/',views.home,name="home"),
   path('mail/',views.mail,name="mail"),
]