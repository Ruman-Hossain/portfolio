from django.db import models

# Create your models here.
class Crud(models.Model):
    id=models.AutoField(primary_key=True)
    device_model=models.CharField(max_length=100,default='ABC')
    device_weight=models.IntegerField(blank=False,default=10)
    device_price=models.IntegerField(blank=False,default=2000)
    # device_image=models.ImageField(upload_to='crud/',blank=False)

    def __str__(self):
        return self.device_model

