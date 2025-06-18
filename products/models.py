from django.db import models

# Create your models here.
class BikeBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} "

class BikeModel(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey(BikeBrand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.model_name} "

class Accessory(models.Model):
    bike_model = models.ForeignKey(BikeModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='accessories/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)
    in_stock = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.name} "

