from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    info = models.info.objects.all()
    return render(request,'index.html',{'info':info})