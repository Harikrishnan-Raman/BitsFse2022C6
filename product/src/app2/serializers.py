from rest_framework import serializers
from .models import products

class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = products 
        fields = ('pk', 'prodName', 'prodDescription', 'prodPrice', 'prodBatch', 'expiryDate', 'isAvailable', 'isPrescriptionRequired')

        
