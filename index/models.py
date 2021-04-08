from django.db import models

class about(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=700,blank=False)
    image=models.ImageField(upload_to='about/',blank=False)

    def __str__(self):
        return self.title

class slider(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,blank=False)
    description=models.TextField(max_length=700,blank=False)
    image=models.ImageField(upload_to='slider/',blank=False)

    def __str__(self):
        return self.title

class service(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,blank=False)
    icon=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=400,blank=False)
    description=models.TextField(max_length=700,blank=False)


    def __str__(self):
        return self.title