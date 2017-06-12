from django.db import models


class Store(models.Model):
    StoreName = models.CharField(blank=True, null=True, max_length=200)
    StoreAddress = models.CharField(max_length=300, null=True, blank=True)
    #StorePhone = models.CharField(max_length=50, null=True, blank=True )

    ContactNo = models.BigIntegerField(null=True, blank=True)
    FirstName = models.CharField(max_length=200, null=True, blank=True)
    LastName = models.CharField(max_length=200, null=True, blank=True)

    Active = models.BooleanField(blank=True, default=True)              # don't know if this is required or not
                                                            # as if store is deleted all its products will be too
    OpeningTime = models.TimeField(null=True, blank=True)
    ClosingTime = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.StoreName





