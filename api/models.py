from django.db import models
#from django.contrib.auth import get_user_model
from django.conf import settings
item_type = (('bottles', 'bottles'), ('cans', 'cans'))
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=100)
    sub_category = models.ManyToManyField('SubCategory', null=True, blank=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    main_category = models.ForeignKey(Category, models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_image = models.ImageField(upload_to ='uploads/')
    price = models.DecimalField(max_digits=7, decimal_places=2,default=0)
    on_discount = models.BooleanField(default=False)
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    type= models.CharField(choices=item_type, max_length=100)
    volume = models.PositiveIntegerField()
    stock = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.item_name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total




    def __str__(self):
        return str(self.product)

