import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.db import models
from crud.models import Category, Product
from django.utils import timezone
from django.contrib.auth.models import User

# Create an admin user
admin_username = 'admin'
admin_email = 'admin@example.com'
admin_password = 'admin'

# Check if the admin user already exists
if not User.objects.filter(username=admin_username).exists():
    User.objects.create_superuser(admin_username, admin_email, admin_password)
    print(f'Admin user "{admin_username}" created.')
else:
    print(f'Admin user "{admin_username}" already exists.')

# Create dummy categories
categories = ['Electronics', 'Books', 'Clothing', 'Home & Kitchen']

for category_name in categories:
    Category.objects.get_or_create(name=category_name)

electronics = Category.objects.get(name='Electronics')
books = Category.objects.get(name='Books')
clothing = Category.objects.get(name='Clothing')
home_kitchen = Category.objects.get(name='Home & Kitchen')

# Create dummy products
products = [
    {'name': 'Laptop', 'price': 800, 'category': electronics, 'description': 'A high performance laptop.', 'image': 'no_image.png'},
    {'name': 'Science Fiction Book', 'price': 15, 'category': books, 'description': 'An exciting sci-fi adventure.', 'image': 'no_image.png'},
    {'name': 'Jeans', 'price': 40, 'category': clothing, 'description': 'Comfortable blue jeans.', 'image': 'no_image.png'},
    {'name': 'Coffee Maker', 'price': 60, 'category': home_kitchen, 'description': 'Make excellent coffee at home.', 'image': 'no_image.png'}
]

for product_info in products:
    product, created = Product.objects.get_or_create(
        name=product_info['name'],
        defaults={
            'price': product_info['price'],
            'category': product_info['category'],
            'description': product_info['description'],
            'image': product_info['image'],
            'created': timezone.now(),  # Use timezone.now() to simulate creation time
            'updated': timezone.now(),  # Use timezone.now() to simulate update time
        }
    )
    if created:
        print(f'Created product: {product.name}')
    else:
        print(f'Product {product.name} already exists.')

print('Dummy data insertion completed.')

