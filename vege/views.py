from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator

from django.contrib.auth import get_user_model

User=get_user_model()



# Create your views here.

def receipe(request):
    if request.method == "POST":
        data=request.POST
        data1=request.FILES
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=data1.get('receipe_image')

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )

        return redirect('/receipe/')
    
    queryset = Receipe.objects.all()
    context = {'receipes': queryset}

    return render(request,'receipe.html',context)

def receipe_delete(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipe/')

def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    context={'receipe': queryset}
    return render(request ,'update_receipe.html',context)

def login_page(request):
    return render(request,"login.html")

def register_page(request):

    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        # print(username)

        user=User.objects.create(
            username=username
        )

        user.set_password(password)
        user.save()


        return redirect('/register/')

    return render(request,"register.html")

from django.db.models import Q,Sum



def get_students(request):
    queryset = Student.objects.all()

    

    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(
            Q(student_name__icontains=search)|
            Q(department__department__icontains=search)|
            Q(student_email__icontains=search)
        )
    
    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)

    
    return render(request,'students.html',{'queryset':page_obj})

def see_marks(request,student_id):
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks=queryset.aggregate(total_marks=Sum('marks'))
    current_ranl=-1
    ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks','student_age')    
    print(queryset)
    return render(request,'report/see_marks.html',{'queryset':queryset,'total_marks':total_marks})