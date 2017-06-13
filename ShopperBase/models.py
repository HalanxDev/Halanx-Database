from django.db import models
from Halanx import settings

AAD = 'Aadhar Card'
VID = 'Voter Id Card'
IdentityProofs = (
    (AAD, 'Aadhar Card'),
    (VID, 'Voter Id Card'),
)


CAR = 'Car'
Vehicles = (
    (CAR, 'Car'),
)


class Shopper(models.Model):

    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    PhoneNo = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=1000, blank=True, null=True)
    EmailId = models.EmailField(blank=True)

    City = models.CharField(max_length=200, null=True, blank=True, default='Delhi')

    IdNumber = models.CharField(max_length=50, blank=True)                             # number of id
    IdType = models.CharField(max_length=100, choices=IdentityProofs, default='Aadhar Card')
    Vehicle = models.CharField(max_length=50, choices=Vehicles, blank=True, default='Car')

    AvgRating = models.FloatField(default=3.0, blank=True, null=True)
    n = models.IntegerField(default=0, blank=True)

    Verified = models.BooleanField(blank=True, default=False)
    AvailableDate = models.DateField(blank=True, null=True)
    AvailableFrom = models.TimeField(blank=True, null=True)
    AvailableTo = models.TimeField(blank=True, null=True)

    A = models.IntegerField(blank=True, default=0)
    B = models.IntegerField(blank=True, default=0)
    C = models.IntegerField(blank=True, default=0)
    D = models.IntegerField(blank=True, default=0)
    E = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.PhoneNo)




