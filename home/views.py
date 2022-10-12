from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments, Doctors
from .forms import BookingForm, ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return render(request, 'confirmation.html')
    form = BookingForm()
    
    dict_form={
        'form': form
    }
    return render(request, 'booking.html', dict_form)
    

def doctors(request):
    dict_docs ={
        'doctors':Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

def contact(request):
    if request.method == 'post':
        form = ContactForm(request.post)
        if form.is_valid():
            form.save()
            print(form)
            return render(request,'endpage.html')
    form = ContactForm()
    
  
    return render(request, 'contact.html', )

def departments(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request, 'departments.html', dict_dept)             
