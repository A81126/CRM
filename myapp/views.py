from django.shortcuts import  render,HttpResponse
from . models import Image

# Create your views here.
def index(request):
    obj=Image.objects.all()
    return render (request,'index.html',{"obj":obj})

