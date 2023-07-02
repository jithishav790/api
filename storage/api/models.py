from django.db import models


# Create your models here.
class Location(models.Model):
    LocaationName=models.CharField(max_length=50)

class Item(models.Model):
    ItemName=models.CharField(max_length=50)
    date_added = models.DateField(auto_now_add=True)
    itemLocation =  models.ForeignKey(Location, on_delete=models.CASCADE)


