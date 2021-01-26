from django.shortcuts import render,HttpResponse
from app01 import models
#https://www.runoob.com/django/django-orm-1.html
# Create your views here.
def index(request):
   return HttpResponse('OS')

def add_book(request):
   books = models.Book.objects.filter(price__lt=210)

   print(books)
   return HttpResponse('os')

