from django.db import models


class Transaction(models.Model):
    orderId = models.IntegerField(max_length=10,default=0)
    orderDate = models.CharField(max_length=10,default='')
    deliveryDate = models.CharField(max_length=10,default='')
    orderStatus = models.CharField(max_length=15,default='')
    noOfItems = models.IntegerField(max_length=10,default=0)
