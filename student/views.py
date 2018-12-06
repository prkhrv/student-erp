from django.shortcuts import render,redirect
from .models import student
from .forms import studentForm
# Create your views here.

def home(request):

    search2 = "none"
    if request.method == 'POST':
            search1 = request.POST.get('search')
            search2 = student.objects.filter(name__contains = search1)
            if search2.count()==0:
                result = "No Records Found"
                search2 = "none"
                return render(request,'index.html',{'result':result,'search2':search2})
            return render(request, 'index.html',{'search2':search2})
    return render(request,"index.html",{'search2':search2})

def register(request):
    success = "Registration Successful"
    form = studentForm()
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, "form.html",{'form':form,'success':success,})
    return render(request, "form.html",{'form':form,})
