from django.db import models

# Create your models here.


class Pokemon(models.Model):
    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=20)
    image = models.CharField(max_length=250)


    def __str__(self):
        return self.name
