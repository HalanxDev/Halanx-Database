from __future__ import unicode_literals

from django.db import models
from ShopperBase.models import Shopper


class Batches(models.Model):
    ShopperId = models.ForeignKey(Shopper, blank=True)
    Earning = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return str(self.ShopperId.PhoneNo) + " : " + str(self.pk)




