from django.db import models
from Products.models import Product
from UserBase.models import User


class Item(models.Model):
    Cart = models.ForeignKey('ItemList', null=True, blank=True )    # add on_delete cascade
    Item = models.ForeignKey(Product)
    Quantity = models.FloatField(blank=True, default=1.0)                   # may be decimal also check
    SubTotal = models.FloatField(blank=True, null=True)
    Notes = models.TextField(null=True, blank=True)
    Active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):  # override save function of model class
        self.SubTotal = self.Item.Price*self.Quantity
        self.Cart.Total = self.Cart.Total + self.SubTotal
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.Item


class ItemList(models.Model):             #object of this class shall be made as soon as the order is placed

    Customer = models.ForeignKey(User, null=True, blank=True)
    Total = models.FloatField(blank=True, null=True, default=0.0)
    timestamp = models.DateTimeField(blank=True, auto_now_add=True)
    Active = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.Total





