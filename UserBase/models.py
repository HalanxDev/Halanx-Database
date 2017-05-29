from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class User(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # UserName = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Address = models.CharField(blank=True, null=True, max_length=300)
    PhoneNo = models.CharField(max_length=50, unique=True)
    EmailId = models.EmailField(blank=True)
    AvgRating = models.FloatField(default=3.0, blank=True, null=True)
    n = models.IntegerField(default=0, blank=True)   #denotes number of times user has been rated

    def __str__(self):
        return self.PhoneNo






