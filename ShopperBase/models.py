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

    AccessToken = models.CharField(max_length=300, blank=True, null=True)

    password = models.CharField(max_length=1000, blank=True, null=True)
    EmailId = models.EmailField(blank=True)

    City = models.CharField(max_length=200, null=True, blank=True, default='Delhi')

    IdNumber = models.CharField(max_length=50, blank=True)                             # number of id
    IdType = models.CharField(max_length=100, blank=True,
                              choices=IdentityProofs,  default='Aadhar Card')

    Vehicle = models.CharField(max_length=50, choices=Vehicles, blank=True, default='Car')

    AvgRating = models.FloatField(default=3.0, blank=True, null=True)
    n = models.IntegerField(default=0, blank=True)

    Verified = models.BooleanField(blank=True, default=False)
    AvailableDate = models.DateField(blank=True, null=True)
    AvailableFrom = models.TimeField(blank=True, null=True)
    AvailableTo = models.TimeField(blank=True, null=True)

    IsOnline = models.BooleanField(blank=True, default=True )
    
    A = models.FloatField(blank=True, default=0)
    B = models.FloatField(blank=True, default=0)
    C = models.FloatField(blank=True, default=0)
    D = models.FloatField(blank=True, default=0)
    E = models.FloatField(blank=True, default=0)

    def __str__(self):
        return str(self.PhoneNo)


class Documents(models.Model):

    ShopperPhoneNo = models.BigIntegerField(unique=True)

    AadharImage = models.TextField(blank=True, null=True)
    LicenseImage = models.TextField(blank=True, null=True)
    VehicleRCImage = models.TextField(blank=True, null=True)

    AadharURL = models.CharField(max_length=500, blank=True, null=True)
    LicenseURL = models.CharField(max_length=500, blank=True, null=True)
    VehicleRCURL = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.ShopperPhoneNo)




