from Home.models import Student
import time

from django.core.mail import send_mail
from django.conf import settings

def run_this_func():
    print("Started")
    time.sleep(2)
    print("Finished") 

def send_email_to_client():
    subject="This email is from django server"
    message="Lawdaaaaa"
    from_email=settings.EMAIL_HOST_USER
    receipt_list=["harshwarghade913@gmail.com"]

    send_mail(subject, message, from_email, receipt_list)


