from unicodedata import name
from django.db import models



class Building(models.Model):
    title=models.CharField(verbose_name="Building Title",max_length=120)

    def __str__(self):
        return self.title


class ApartmentType(models.Model):

    type=models.CharField(verbose_name="type",max_length=5)

    def __str__(self):
        return self.type

    



class Apartment(models.Model):
    name=models.CharField(verbose_name="Apartment Name" , max_length=130)

    description=models.CharField(verbose_name="Description",max_length=200)

    apartment_type=models.ForeignKey("ApartmentType",on_delete=models.CASCADE ,null=True)

    building=models.ForeignKey("Building",on_delete=models.CASCADE)


    def __str__(self):
        return self.name