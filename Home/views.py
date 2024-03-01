from django.shortcuts import render,redirect
from django.http import HttpResponse
from .utils import send_email_to_client
# Create your views here.

def send_email(request):
    send_email_to_client
    return redirect('/')


def home(request):
    return render(request,"Home\index.html")

def contact(request):
    return render(request,"Home\contact.html")
def about(request):
    return render(request,"Home\about.html")

def success_page(request):
    return HttpResponse("THis is a success page")

# def receipe(request):
#     return render(request,"vege/templates/receipe.html")