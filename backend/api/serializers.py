from rest_framework import serializers
from api.models import Customers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['name', 'phone_num', 'product']