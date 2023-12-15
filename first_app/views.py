from django.shortcuts import render
from . forms import ContactForm
from . import models
# Create your views here.
def home(request):
    return render(request,'home.html')

def form(request):
    form=ContactForm(request.POST)
    if form.is_valid:
        return render(request,'form.html', {'form':form})
def model(request):
    student=models.Student.objects.all()
    return render (request,"model.html",{'data':student})