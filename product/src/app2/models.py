from django.db import models

class products(models.Model):
    prodName = models.CharField(max_length=240)
    prodDescription = models.CharField(max_length=1024)
    prodPrice = models.CharField(max_length=20)
    prodBatch = models.CharField(max_length=20)
    expiryDate = models.CharField(max_length=20)
    isAvailable = models.BooleanField(default=True)
    isPrescriptionRequired = models.BooleanField(default=False)

