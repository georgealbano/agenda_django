import email
import site
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q
from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone',


def create(request):
    if request.method == 'POST':
        print(request.POST)
        print('estou no POST')
        context = {
            'form': ContactForm(request.POST)
        }  
        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm()
    }
    return render(
        request,
        'contact/create.html',
        context
    )
