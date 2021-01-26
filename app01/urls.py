from django.urls import path,include
from app01 import views
urlpatterns = [
    path('',views.index),
    path('add_book/',views.add_book),

]