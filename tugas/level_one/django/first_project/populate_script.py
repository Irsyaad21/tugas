import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import ShoesType, Shoes, OwnerRecord
from faker import Faker
from datetime import datetime


django.setup()


fake = Faker()
Shoes_type = ['Adidas', 'Nike', 'Puma']

def add_shoes_type():
    for vt in Shoes_type:
        Shoes_type.objects.get_or_create(type_name=vt)

def populate(n=5):
    add_shoes_type()

    for _ in range(n):
        Shoes_type = ShoesType.objects.order_by('?').first()

        
        owner_name = fake.name()
        color = fake.color_name()
        vin = fake.bothify(text="??#########???????")  

        
        Shoes, created = Shoes.objects.get_or_create(
            Shoes_type=Shoes_type,
            owner_name=owner_name,
            color=color,
            vin=vin
        )
      

if __name__ == '__main__':
    print("Populating script...")
    populate(20) 
    print("Complete!")
