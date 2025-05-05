from django.urls import path
from qp_app.views import get_ExpenseAdded, get_products, create_product, get_categories, create_category, delete_category,get_companies, create_company, delete_company



urlpatterns = [
    path('expenses/', get_ExpenseAdded),
    path('all_products/', get_products),
    path('create_product/', create_product),

    #Categories
    path('get_categories/', get_categories),
    path('create_category/', create_category),
    path('delete_category/', delete_category),

    #Companies
    path('get_companies/', get_companies),
    path('create_company/', create_company),
    path('delete_company/', delete_company),

    
]

