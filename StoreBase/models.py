from django.db import models
from Products.models import Product


class Store(models.Model):

    ProductsAvailable = models.ManyToManyField(Product, blank=True)
    StoreName = models.CharField(blank=True, null=True, max_length=200)
    StoreAddress = models.CharField(max_length=300, null=True, blank=True)

    Dealer_FirstName = models.CharField(max_length=200, null=True, blank=True)
    Dealer_LastName = models.CharField(max_length=200, null=True, blank=True)
    Dealer_ContactNo = models.BigIntegerField(null=True, blank=True)
    Dealer_EmailId = models.EmailField(blank=True, null=True)
    Dealer_password = models.CharField(max_length=1000, blank=True, null=True)

    Latitude = models.FloatField(blank=True, null=True)
    Longitude = models.FloatField(blank=True, null=True)

    Active = models.BooleanField(blank=True, default=True)              # don't know if this is required or not
                                                            # as if store is deleted all its products will be too
    OpeningTime = models.TimeField(null=True, blank=True)
    ClosingTime = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.StoreName





