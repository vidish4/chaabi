from rest_framework import serializers
from .models import Drinks
from .models import Product

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id','name','description']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['index','product','category','sub_category','brand','sale_price','market_price','type','rating','description','vector']