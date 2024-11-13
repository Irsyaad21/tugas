from django.db import model

# Create your models here.

class ShoesType(models.Model):
    type_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.type_name


class Shoes(models.Model):
    shoes_type = models.ForeignKey(ShoesType, on_delete=models.CASCADE)
    owner = models.CharField(max_length=264)
    license_plate = models.CharField(max_length=15, unique=True)
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=17, unique=True)  

    def __str__(self):
        return f"{self.license_plate} - {self.owner}"


class OwnerRecord(models.Model):
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.shoes} - {self.purchase_date}"