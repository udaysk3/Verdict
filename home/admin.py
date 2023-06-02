from django.contrib import admin
from .models import Brand, Product, Category,Electronic_Review,Place_Review,City,Place
# Register your models here.
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Electronic_Review)
admin.site.register(Place_Review)
admin.site.register(City)
admin.site.register(Place)