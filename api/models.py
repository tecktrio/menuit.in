from django.db import models

# Create your models here.
class ShopOwners(models.Model):
    user_name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 20)
    email_id = models.EmailField()
    contact_number = models.IntegerField()
    isBlocked = models.BooleanField(default = False)
    
    def __str__(self) -> str:
        return self.user_name
    
    class Meta:
        verbose_name_plural = 'ShopOwners'
        app_label = 'api'
    
        
class Stores(models.Model):
    store_name              = models.CharField(max_length = 50, null = False)
    store_license_number    = models.CharField(max_length = 50, null = False)
    store_owner             = models.ForeignKey(ShopOwners, on_delete = models.CASCADE)
    store_rating            = models.IntegerField(default = 5)
    store_desription        = models.TextField()
    store_image_url         = models.TextField()
    store_open_dates        = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name_plural = 'Stores'    
        app_label = 'api'

class Customers(models.Model):
    customer_name            = models.CharField(max_length = 50)
    customer_contact_number  = models.CharField(max_length = 10)
    customer_email           = models.EmailField()
    belongs_to_the_store     = models.ForeignKey(Stores, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.contact_number
    
    class Meta:
        verbose_name_plural = 'Customers'
        app_label = 'api'
        
            
class Categories(models.Model):
    category_name            = models.CharField(max_length = 50, null = False)
    category_description     = models.TextField()
    category_image_url       = models.TextField()
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Categories'    
        app_label = 'api'  
        
              
class Division(models.Model):
    division_name = models.CharField(max_length = 100)
    division_store = models.ForeignKey(Stores, on_delete = models.CASCADE)
    division_unique_id = models.IntegerField(default = 0000000000)
    
    def __str__(self) -> str:
        return self.division_store.store_name
    class Meta:
        verbose_name_plural = 'division'
        app_label = 'api'
          
class Products(models.Model):
    product_unique_id       = models.CharField(max_length = 50, null = False)
    product_name            = models.CharField(max_length = 50, null = False)
    product_category        = models.ForeignKey(Categories, on_delete = models.CASCADE )
    product_price           = models.IntegerField()
    product_rating          = models.IntegerField(default = 5)
    product_description     = models.TextField()
    product_image_url       = models.TextField()
    product_available       = models.IntegerField(default = 0)
    product_division        = models.ForeignKey(Division, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.product_unique_id
    
    class Meta:
        verbose_name_plural = 'Products'   
        app_label = 'api' 

        
class Advertisments(models.Model):
    ad_unique_id    = models.CharField(max_length = 50)
    ad_type         = models.CharField(max_length = 50, choices = (('banner','banner'),('video','video')))
    ad_url          = models.TextField()
    ad_store        = models.ForeignKey(Stores, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.ad_unique_id
    
    class Meta:
        app_label = 'api'