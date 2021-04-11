from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    slug = models.SlugField(max_length=40)
    thumbnail = models.ImageField(upload_to='media/products/thumbnails')
    file = models.FileField(upload_to='media/products/files')
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    file_size = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status_choices = (
        ("SUCCESS", "SUCCESS"),
        ("FAIL", "FAIL"),
    )
    status = models.CharField(choices=status_choices, max_length=10)
    payment_id = models.CharField(max_length=40, null=True, blank=True)
    order_id = models.CharField(max_length=40, null=True, blank=True)


class UserProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
