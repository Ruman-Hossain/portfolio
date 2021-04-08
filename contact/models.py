from django.db import models

# Create your models here.


class contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, blank=False)
    email=models.CharField(max_length=100,blank=False)
    subject=models.TextField(max_length=800,blank=False)
    message=models.TextField(max_length=800,blank=False)

    def __str__(self):
        return self.subject