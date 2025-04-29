from django.urls import path
from qp_app.views import get_ExpenseAdded, get_products, create_product

urlpatterns = [
    path('expenses/', get_ExpenseAdded),
    path('all_products/', get_products),
    path('create_product/', create_product),
]
