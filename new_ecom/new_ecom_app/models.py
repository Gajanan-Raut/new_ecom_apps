from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    
    is_delete =models.CharField(max_length=5, default='N')
    def __str__(self):
        return self.name
    