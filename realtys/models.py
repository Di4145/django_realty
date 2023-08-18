from django.db import models

# Create your models here.
class RealtyType(models.Model):
    type = models.CharField(max_length=40)

class RealtyManager(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='image_manager')


class Realty(models.Model):
    type = models.ForeignKey(RealtyType, on_delete=models.PROTECT)
    cost = models.IntegerField()
    s = models.DecimalField(decimal_places=8, max_digits=8)
    info = models.TextField()
    image_cover = models.ImageField(upload_to='image_cover')
    manager = models.ForeignKey(RealtyManager, on_delete=models.PROTECT)


