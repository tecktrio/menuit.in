from .models import  Division, ShopOwners
from .models import Products
from .models import Stores
from .models import Customers
from .models import Categories
from rest_framework.serializers import ModelSerializer

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = ['customer_name','customer_contact_number','customer_email']
        
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        
class ShopOwnerSerializer(ModelSerializer):
    class Meta:
        model = ShopOwners
        fields = '__all__'
        
                
class StoreSerializer(ModelSerializer):
    class Meta:
        model = Stores
        fields = '__all__'
        
                
                
class DivisionSerializer(ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'
        
        