from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    publish = models.CharField(max_length=32)
    pub_date = models.DateField()
