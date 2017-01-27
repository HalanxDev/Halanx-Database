from django.db import models
from ItemsList.models import ItemList
from ShopperBase.models import Shopper
from BatchBase.models import Batches


RatingChoice = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

# Problem : How to update shopper and user ratings after order is delivered ?   Done


class Order (models.Model):

    OrderId = models.IntegerField(unique=True)  # maybe not needed cos pk of class would have the same function

    Items = models.OneToOneField(ItemList, blank=True)                # check
    BatchId = models.ForeignKey(Batches, blank=True)
    ShopperId = models.ForeignKey(Shopper, null=True, blank=True)

    Total = models.FloatField(null=True)
    DeliveryCharge = models.FloatField(null=True, blank=True, default=0.0)

    PlacingTime = models.DateTimeField(auto_now_add=True)
    DeliveryAddress = models.CharField(max_length=300, null=True)
    Earnings = models.FloatField(null=True, blank=True, default=0.0)

    UserRating = models.IntegerField(choices=RatingChoice, default=3)
    ShopperRating = models.IntegerField(choices=RatingChoice, default=3)

    IsDelivered = models.BooleanField(default=False)

    DeliveryDate = models.DateField(null=True, blank=True)
    StartTime = models.TimeField(null=True, blank=True)
    EndTime = models.TimeField(null=True, blank=True)

    Notes = models.TextField(null=True, blank=True)
    PriorityScore = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.OrderId

    def save(self, *args, **kwargs):  # override save function of model class
        self.Total = self.Items.Total
        # attach code for earnings of shopper in this order

        if self.IsDelivered == True:
            temp = self.ShopperId.AvgRating*self.ShopperId.n
            temp1 = self.Items.Customer.AvgRating*self.Items.Customer.n
            self.ShopperId.n +=1
            self.Items.Customer.n +=1
            temp += self.ShopperRating
            temp1 += self.UserRating
            self.ShopperId.AvgRating /= self.ShopperId.n
            self.Items.Customer.AvgRating /=self.Items.Customer.n

        self.BatchId.Earning += self.Earnings
        super(Order, self).save(*args, **kwargs)





