from rest_framework import serializers 
from .models import ExpenseModel, Product, Category, Company
from django.contrib.auth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['username','email','password']
    
    def create(self, validated_data):
        user= User(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Mets:
        model = User
        fields = ['username']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseModel
        fields = ['id', 'date', 'supplier', 'tax', 'payment_type', 'category', 'description', 'added_by']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','barcode','product_name','category','company_name','buying_price','selling_price','quantity','tax_percentage']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name']
        