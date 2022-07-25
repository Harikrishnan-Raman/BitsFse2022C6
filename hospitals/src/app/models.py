from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=30,default='')
    contact = models.CharField(max_length=10,default='')
    address = models.CharField(max_length=60,default='')
