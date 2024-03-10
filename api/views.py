from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import Customers, Products
from . models import Division
from . models import Categories
from . models import ShopOwners
from . models import Stores
from .serializers import  DivisionSerializer, ShopOwnerSerializer, StoreSerializer
from .serializers import ProductSerializer
from .serializers import CategorySerializer
# Create your views here.

InvalidDataError = 204
ItemNotFound = 201
ActionNotAllowed =202
NotEnoughData = 203
Success = 200
Exist = 204

class ManageProducts(APIView):
    def get(self, request):
        shop_owner_username = request.query_params.get('shop_owner_username')
        store_name = request.query_params.get('store_name')
        division_name = request.query_params.get('division_name')
        
        
        print(shop_owner_username, store_name, division_name)
        shop_owner = ShopOwners.objects.filter(user_name=shop_owner_username).first()
        if shop_owner:
            store = Stores.objects.filter(store_owner=shop_owner, store_name=store_name).first()
            if store:
                division = Division.objects.filter(division_store=store, division_name=division_name).first()
                if division:
                    products = Products.objects.filter(product_division=division)
                    if 'price' in request.query_params:
                        print('applying price filter')
                        price_filter = request.query_params.get('price')
                        products = products.filter(product_price__lt = price_filter)
                        
                    if 'category' in request.query_params:
                        print('applying category filter')
                        category_filter = request.query_params.get('category')
                        products = products.filter(product_category = category_filter)
                        
                    serialized_products = ProductSerializer(products, many=True)
                    return Response(serialized_products.data, status = 200)
                else:
                    return Response(status = 404)
            else:
                return Response(status = 404)
        else:
            return Response(status = 404)
    
    def post(self, request):
        try:
            product_name = request.data['product_name']
            product_price = request.data['product_price']
            product_category = request.data['product_category']
            product_description = request.data['product_description']
            product_image_url = request.data['product_image_url']
            product_unique_id = request.data['product_unique_id']
            product_division_id = request.data['product_division']
            
            product = Products.objects.filter(product_unique_id = product_unique_id).first()
            if product:
                return Response({"reason":"product already exist"}, status=500)
            
            category = Categories.objects.get(category_name = product_category)
            product_division = Division.objects.get(id = product_division_id)
            
            Products.objects.create(
                product_name = product_name,
                product_category = category, 
                product_description = product_description,
                product_image_url = product_image_url,
                product_unique_id = product_unique_id,
                product_price = product_price,
                product_division = product_division
            ).save()
            return Response(status=200)
            
        except Exception as e:
            return Response({'reason':e}, status=500)
    
    def put(self, request):
        try:
            key1 = request.data['key']
            value = request.data['value']
            product_unique_id = request.data['product_unique_id']
            try:
                product = Products.objects.get(product_unique_id=product_unique_id)
            except Products.DoesNotExist:
                return Response(status=404)

            # Update the field dynamically
            setattr(product, key1, value)
                
            try:
                product.save()
            except:
                return Response(status=500)

            
        except:
            return Response(status=404)
    
    def delete(self, request):
        product_unique_id = request.query_params.get('product_unique_id')
        if Products.objects.filter(product_unique_id = product_unique_id).exist():
            product = Products.objects.get(product_unique_id = product_unique_id)
            try:
                product.delete()
                return Response(status=200)
            except:
                return Response(status=404)
        else:
            return Response(status=404)
        
        
class ManageCustomers(APIView):
    def get(self, request):
        # customers = Customers.objects.all()
        # serialized_customers = CustomerSerializer(customers, many = True)
        # return Response({'status':202, 'data':serialized_customers.data})  
        pass
    def post(self, request):
         customer_name = request.data['customer_name']
         customer_contact_number = request.data['customer_contact_number']
         customer_email = request.data['customer_email']
         
        #  customer = Customers.objects.create(
        #      customer_name = customer_name,
        #      customer_contact_number = customer_contact_number, 
        #      customer_email = customer_email)
        #  try:
        #      customer.save()
        #  except:
        #      return Response({'status':InvalidDataError})
         
    def put(self, request):
        customer_id = request.data['customer_id']
        customer_name = request.data['customer_name']
        customer_contact_number = request.data['customer_contact_number']
        customer_email = request.data['customer_email']
        
        # if Customers.objects.filter(id= customer_id).exists():
        #     customer = Customers.objects.get(id = customer_id)
        #     customer.customer_name = customer_name
        #     customer.customer_contact_number = customer_contact_number
        #     customer.customer_email = customer_email
            
        #     try:
        #         customer.save()
        #     except:
        #         return Response({'status':InvalidDataError})
        # else:
        #     return Response({'status':ItemNotFound})
     
class ManageCategories(APIView):
    def get(self, request):
        categories = Categories.objects.all()
        serialized_categories = CategorySerializer(categories, many = True)
        return Response({'status':202, 'data':serialized_categories.data})
    
    def post(self, request):
        try:
            category_name = request.data['category_name']
            category_description = request.data['category_description']
            category_image_url = request.data['category_image_url']
            
            if Categories.objects.filter(category_name = category_name).exists():
                return Response({'status':Exist})
            
            category = Categories.objects.create(
                category_name = category_name, 
                category_description = category_description, 
                category_image_url = category_image_url
            )
            
            try:
                category.save()
            except:
                return Response({'status':InvalidDataError})
            return Response({'status':Success})
        except:
            return Response({'status':NotEnoughData, 'reason':'Required Fields [ category_name, category_description, category_image_url ]'})
    def put(self, request):
        category_id = request.data['category_id']
        category_name = request.data['category_name']
        category_price = request.data['category_price']
        category_description = request.data['category_description']
        category_image_url = request.data['category_image_url']
        
        if Categories.objects.filter(id = category_id).exists():
            category = Categories.objects.get(id = category_id)
            category.category_name = category_name
            category.category_price = category_price
            category.category_description  = category_description
            category.category_image_url = category_image_url
            
            try:
                category.save()
            except:
                return Response({'status':InvalidDataError})
        else:
            return Response({'status':ItemNotFound})
        
    def delete(self, request):
        try:
            category_id = request.data['category_id']
            if Categories.objects.filter(id = category_id).exists():
                category = Categories.objects.get(id = category_id)
                try:
                    category.delete()
                    return Response({'status':Success})
                except:
                    return Response({'status':ActionNotAllowed})
            else:
                return Response({'status':ItemNotFound})
        except Exception as e:
            return Response({'status':InvalidDataError, 'reason':e})
        
        
class ManageShopOwners(APIView):
    
    def get(self, request):
        if ShopOwners.objects.filter(id = request.query_params.get('shop_owner_id')).exists():
            shopOwner = ShopOwners.objects.get(id = request.query_params.get('shop_owner_id'))
            serialized_shopOwner = ShopOwnerSerializer(shopOwner, many = False)
            return Response({'status':Success, 'data':serialized_shopOwner.data})
        else:
            return Response({'status':ItemNotFound})
        
    def post(self, request):
        try:
            user_name = request.data['user_name']
            password = request.data['password']
            email_id = request.data['email_id']
            contact = request.data['contact']
            
            shopOwner = ShopOwners.objects.create( user_name = user_name, password = password, email_id = email_id, contact_number = contact)
            # print(user_name)
            try:
                shopOwner.save()
                return Response({'status':Success})
                
            except:
                return Response({'status':InvalidDataError})
        except Exception as e:
            return Response({'status':InvalidDataError,'reason': e})
  
    def put(self, request):
        shop_owner_id = request.data['shop_owner_id']
        field = request.data['field']
        value = request.data['value']
            
        if ShopOwners.objects.filter(id = shop_owner_id).exists():
            shopOwner = ShopOwners.objects.get(id = shop_owner_id)
            
            
            
            return Response({'status':Success})
    def delete(self, request):
        pass
    
    
class ManageStore(APIView):
  
    def get(self, request):
        if Stores.objects.filter(id = request.query_params.get('store_id')).exists():
            shopOwner = Stores.objects.get(id = request.query_params.get('store_id'))
            serialized_store = StoreSerializer(shopOwner, many = False)
            return Response({'status':Success, 'data':serialized_store.data})
        else:
            return Response({'status':ItemNotFound})
        
    def post(self, request):
        try:
            store_name = request.data['store_name']
            store_license_number = request.data['store_license_number']
            store_owner_id = request.data['store_owner_id']
            store_description = request.data['store_description']
            store_image_url = request.data['store_image_url']
            store_open_dates = request.data['store_open_dates']
            
            store_owner = ShopOwners.objects.get(id = store_owner_id)
            
            store = Stores.objects.create( store_name = store_name,
                                          store_license_number = store_license_number,
                                          store_desription = store_description,
                                          store_image_url = store_image_url,
                                          store_owner = store_owner,
                                          store_open_dates = store_open_dates)
            # print(user_name)
            try:
                store.save()
                return Response({'status':Success})
                
            except:
                return Response({'status':InvalidDataError})
        except Exception as e:
            return Response({'status':InvalidDataError,'reason': e})
  
    def put(self, request):
        shop_owner_id = request.data['shop_owner_id']
        field = request.data['field']
        value = request.data['value']
            
        if ShopOwners.objects.filter(id = shop_owner_id).exists():
            shopOwner = ShopOwners.objects.get(id = shop_owner_id)
            
            
            
            return Response({'status':Success})
    def delete(self, request):
        pass
    
    
class ManageDivision(APIView):
    def get(self, request):
        if Division.objects.filter(id = request.query_params.get('division_id')).exists():
            shopOwner = Division.objects.get(id = request.query_params.get('division_id'))
            serialized_division = DivisionSerializer(shopOwner, many = False)
            return Response({'status':Success, 'data':serialized_division.data})
        else:
            return Response({'status':ItemNotFound})
        
    def post(self, request):
        try:
            division_name = request.data['division_name']
            division_store_id = request.data['division_store_id']
            # division_unique_id = request.data['division_unique_id']
           
            
            store = Stores.objects.get(id = division_store_id)
            
            division = Division.objects.create( division_name = division_name,
                                          division_store = store,
                                         )
            # print(user_name)
            try:
                store.save()
                return Response({'status':Success})
                
            except:
                return Response({'status':InvalidDataError})
        except Exception as e:
            return Response({'status':InvalidDataError,'reason': e})
  
    def put(self, request):
        shop_owner_id = request.data['shop_owner_id']
        field = request.data['field']
        value = request.data['value']
            
        if Division.objects.filter(id = shop_owner_id).exists():
            shopOwner = Division.objects.get(id = shop_owner_id)
            
            
            
            return Response({'status':Success})
    def delete(self, request):
        pass
    