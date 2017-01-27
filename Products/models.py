from django.db import models
from StoreBase.models import Store


SHOE = 'Footwear'
DRY = 'Dairy Products'
NONE = 'No specific category'


ProductCategories = (            # Add categories here
(SHOE, 'Footwear'),
(DRY, 'Dairy Products'),
(NONE, 'No Specific Category'),
)


class Product(models.Model):

    StoreId = models.ManyToManyField(Store, blank=True)
    ProductName = models.CharField(blank=True, max_length=250)
    Price = models.FloatField(blank=True, default=9.99)

    Category = models.CharField(max_length=200,
                                choices=ProductCategories,
                                blank=True, null=True,
                                default='No Specific Category')

    ProductImage = models.ImageField(upload_to="productimg/", null=True, blank=True)
    Features = models.TextField(blank=True, null=True)
    Active = models.BooleanField(blank=True, default=True)    # no need of this as only active products will be stred in DB

    def __str__(self):
        return self.ProductName


    #No need of this
    #def save(self, *args, **kwargs):

        #attach algo for delivery charges
     #   super(CartItem, self).save(*args, **kwargs)




