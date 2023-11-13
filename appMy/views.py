from django.shortcuts import render
from .models import *

def indexPage(request):
   carousel_list = Carousel.objects.all()
   context={
      "carousel_list":carousel_list,
   }
   return render(request,'index.html', context)
def contactPage(request):
   context={}
   return render(request,'contact.html', context)





