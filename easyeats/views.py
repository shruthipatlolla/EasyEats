# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class AboutPageView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'aboutus.html'

class ContactPageView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'contact.html'

class MenuPAgeView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'menu.html'

class ProfilePageView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'profile.html'





def emailView(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['pshruthi98@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def successView(request):

    return HttpResponse('Success! Thank you for your message.')
