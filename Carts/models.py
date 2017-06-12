from django.db import models
from Products.models import Product
from UserBase.models import User


class CartItem(models.Model):
    Cart = models.ForeignKey('Cart', null=True, blank=True, default=1, related_name="carts")    # add on_delete cascade
    Item = models.ForeignKey(Product)
    # CartNo = models.IntegerField(blank=True, default=1)
    # there is no need for this .. rectify error in views_cart_items
    
    Quantity = models.FloatField(blank=True, default=1.0)                   # may be decimal also check
    SubTotal = models.FloatField(blank=True, null=True)
    Notes = models.TextField(null=True, blank=True)
    Active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.SubTotal = self.Item.Price * self.Quantity
        self.Cart.Total = self.Cart.Total + (self.Item.Price*self.Quantity)
        # self.CartNo = self.Cart.pk
        super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.Cart.UserPhone) + " : " + str(self.Item.pk)


class Cart(models.Model):             # object of this class shall be updated as soon as user changes his cart

    Username = models.OneToOneField(User, blank=True, null=True)
    Total = models.FloatField(blank=True, default=0.0)
<<<<<<< HEAD
    UserPhone = models.BigIntegerField(unique=True, null=True, blank=True)
=======
    UserPhone = models.BigIntegerField(unique=True, null=True)
>>>>>>> 00fb1996c369d73bf36067bf3cd8aca96e95305e
    # AllItems = models.ManyToManyField(CartItem, blank=True)
    # not req. but nothing else working

    DeliveryCharges = models.FloatField(blank=True, default=0.0)
    timestamp = models.DateTimeField(blank=True, auto_now=True)     # timestamp change as soon as cart changes
    Active = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return str(self.Username.PhoneNo)

    def save(self, *args, **kwargs):

        self.UserPhone = self.Username.PhoneNo

        # attach algo for delivery charges
        super(Cart, self).save(*args, **kwargs)














