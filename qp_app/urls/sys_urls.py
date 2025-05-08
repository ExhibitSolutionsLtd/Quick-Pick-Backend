from django.urls import path
from qp_app.views import (
    # Expense 
    get_ExpenseAdded,
    # Product 
    get_products, create_product,
    # Category 
    get_categories, create_category, edit_category, delete_category,
    # Company 
    get_companies, create_company, edit_company, delete_company,
    # Role 
    get_roles, create_role, edit_role, delete_role,
    # Payment type 
    get_payment_types, create_payment_type, edit_payment_type, delete_payment_type,
    #Customer
    get_customers, create_customer, delete_customer, edit_customer
)



urlpatterns = [
    path('expenses/', get_ExpenseAdded),
    path('all_products/', get_products),
    path('create_product/', create_product),

    #Categories
    path('get_categories/', get_categories),
    path('create_category/', create_category),
    path('delete_category/', delete_category),
    path('edit_category/', edit_category),

    #Companies
    path('get_companies/', get_companies),
    path('create_company/', create_company),
    path('delete_company/', delete_company),
    path('edit_company/', edit_company),

    #Roles
    path('get_roles/', get_roles),
    path('create_role/', create_role),
    path('delete_role/', delete_role),
    path('edit_role/', edit_role),

    # Payment Types
    path('get_payment_types/', get_payment_types),
    path('create_payment_type/', create_payment_type),
    path('delete_payment_type/', delete_payment_type),
    path('edit_payment_type/', edit_payment_type),
    
    #Customers
    path('get_customers/', get_customers),
    path('create_customer/', create_customer),
    path('delete_customer/', delete_customer),
    path('edit_customer/', edit_customer),
]




