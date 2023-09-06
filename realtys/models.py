from django.db import models

# Create your models here.
class RealtyType(models.Model):
    type = models.CharField(max_length=40)

    def __str__(self):
        return self.type

class RealtyManager(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='image_manager')

    def __str__(self):
        return self.name


class Realty(models.Model):
    header = models.CharField(max_length=40, null=True, blank=True)
    type = models.ForeignKey(RealtyType, on_delete=models.PROTECT)
    cost = models.IntegerField()
    s = models.DecimalField(decimal_places=1, max_digits=8)
    info = models.TextField()
    image_cover = models.ImageField(upload_to='image_cover')
    manager = models.ForeignKey(RealtyManager, on_delete=models.PROTECT)


