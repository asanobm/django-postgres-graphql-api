from django.db import models


# Create your models here.


class Shop(models.Model):
    name = models.TextField(unique=True)
    url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Thumbnail(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.BinaryField()


class Item(models.Model):
    name = models.CharField(max_length=200)
    thumbnail = models.ForeignKey(Thumbnail, on_delete=models.CASCADE)
    seller = models.ForeignKey(Shop, on_delete=models.CASCADE)
    url = models.CharField(max_length=2083)
    description = models.TextField()
    page = models.TextField()
