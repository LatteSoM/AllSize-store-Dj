from rest_framework import serializers
from .models import Brands, Category, Colors, Sizes, Goods, HugeCard, MainCats, MainBrands, MainProducts, SizesToGoodTable, Images


class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizes
        fields = '__all__'


class SizeToGoodTablesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizesToGoodTable
        fields = '__all__'


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GoodssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = '__all__'
