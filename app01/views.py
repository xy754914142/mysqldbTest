from django.shortcuts import render,HttpResponse
#https://www.runoob.com/django/django-orm-1.html
# Create your views here.
def index(request):
   return HttpResponse('OS')