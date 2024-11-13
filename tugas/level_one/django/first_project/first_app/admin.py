from django.contrib import admin
from .models import ShoesType, Shoes, OwnerRecord

# Register your models here.
admin.site.register(ShoesType)
admin.site.register(Shoes)
admin.site.register(OwnerRecord)
