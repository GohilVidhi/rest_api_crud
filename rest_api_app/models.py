from django.db import models

# Create your models here.




class user(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    




