from django.test import TestCase

# Create your tests here.
from django.urls import path
from .views import ManageProducts, ManageCustomers,ManageDivision,  ManageCategories , ManageShopOwners, ManageStore
urlpatterns = [
    # path('',view=ManageProducts.as_view()),
    path('products',view=ManageProducts.as_view()),
    path('categories',view=ManageCategories.as_view()),
    path('customers',view=ManageCustomers.as_view()),
    path('shop_owners',view=ManageShopOwners.as_view()),
    path('store',view=ManageStore.as_view()),
    path('division',view=ManageDivision.as_view()),
] 