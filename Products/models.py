from django.db import models
from StoreBase.models import Store


SHOE = 'Footwear'
DRY = 'Dairy Products'
FUR = 'Furniture'
FOOD = 'Food'
NONE = 'No specific category'


ProductCategories = (            # Add categories here
 (SHOE, 'Footwear'),
 (DRY, 'Dairy Products'),
 (FUR, 'Furniture'),
 (FOOD, 'Food'),
 (NONE, 'No Specific Category'),
)


class Product(models.Model):

    ProductName = models.CharField(blank=True, max_length=250)
    Price = models.FloatField(blank=True, default=9.99)
    StoreId = models.ForeignKey(Store, blank=True, null=True)

    # choices = ProductCategories
    Category = models.CharField(max_length=200,
                                blank=True, null=True,
                                default='No Specific Category')

    ProductImage = models.CharField(max_length=400, null=True, blank=True)
    Features = models.TextField(blank=True, null=True)
    ProductSize = models.IntegerField(blank=True, null=True, default=3)

    Active = models.BooleanField(blank=True, default=True)    # no need of this as only active products will be stred in DB

    def __str__(self):
        return self.ProductName


    #No need of this
    #def save(self, *args, **kwargs):

        #attach algo for delivery charges
     #   super(CartItem, self).save(*args, **kwargs)


class ProductPhoto(models.Model):

    ProductId = models.IntegerField(unique=True, blank=True, null=True)

    ProductString = models.TextField(blank=True, null=True)

    def __str__(self):

        return str(self.ProductId)





















