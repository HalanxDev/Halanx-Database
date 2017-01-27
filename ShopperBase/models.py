from django.db import models


AAD = 'Aadhar Card'
VID = 'Voter Id Card'
IdentityProofs = (
    (AAD,'Aadhar Card'),
    (VID,'Voter Id Card'),
)


CAR = 'Car'
Vehicles = (
    (CAR, 'Car'),
)


class Slot(models.Model):

    Date = models.DateField(null=True, blank=True)
    StartTime = models.TimeField(null=True, blank=True)
    EndTime = models.TimeField(null=True, blank=True)

    def __str__(self):
        return str(self.Date) + " : " + str(self.StartTime) + " to " + str(self.EndTime)


class Shopper(models.Model):

    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    PhoneNo = models.CharField(max_length=50, unique=True)
    EmailId = models.EmailField(blank=True)
    City = models.CharField(max_length=200, null=True, blank=True, default='Delhi')
    IdNumber = models.CharField(max_length=50, blank=True)                             # number of id
    IdType = models.CharField(max_length=100, choices=IdentityProofs, default='Aadhar Card')
    Vehicle = models.CharField(max_length=50, blank=True, default='Car')
    AvgRating = models.FloatField(default=3.0, blank=True, null=True)
    n = models.IntegerField(default=0, blank=True)

    AvailableSlots = models.ManyToManyField(Slot, blank=True, default= 1)

    A = models.IntegerField(blank=True, default=0)
    B = models.IntegerField(blank=True, default=0)
    C = models.IntegerField(blank=True, default=0)
    D = models.IntegerField(blank=True, default=0)
    E = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.PhoneNo




