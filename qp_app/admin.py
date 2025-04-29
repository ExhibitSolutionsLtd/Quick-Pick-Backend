from django.contrib import admin
from qp_app.models import ExpenseModel, PaymentType, Supplier, Category, Company, Product, Shop, UserProfile, Purchase, Customer, Role

admin.site.register(Product)
admin.site.register(ExpenseModel)
admin.site.register(PaymentType)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(UserProfile)
admin.site.register(Purchase)
admin.site.register(Customer)
admin.site.register(Role)
admin.site.register(Company)
