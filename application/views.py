from django.shortcuts import render
from application import *
from application.models import enquiry_table
from django.contrib import messages
# Create your views here.
def home(request):
   
    return render (request,'index.html')

def portfolio(request):
    return render (request,'portfolio.html')

def contact(request):
    if request.method == "POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('subject')
        d=request.POST.get('message')
        enquiry = enquiry_table(name = a, email = b, subject = c, message = d)
        enquiry.save()
        messages.success(request, 'Enquiry Form Submitted Successfully...')
    return render(request,'contact.html')


def services(request):
    return render (request,'services.html')
    