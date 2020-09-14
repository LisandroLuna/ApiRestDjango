from django.db import models


class Phone(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    img = models.CharField(max_length=500, default='')
    desc = models.CharField(max_length=1000, default='')

    def __str__(self):
        return str(self.brand) + ' ' + str(self.model)
