from django.db import models


class User(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # UserName = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    PhoneNo = models.BigIntegerField(unique=True, null=True)
    EmailId = models.EmailField(blank=True)
    FirstName = models.CharField(max_length=200, blank=True)
    LastName = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=1000, null=True)
    Address = models.CharField(blank=True, null=True, max_length=300)
    AvgRating = models.FloatField(default=3.0, blank=True)
    n = models.IntegerField(default=0, blank=True)     # denotes number of times user has been rated

    def __str__(self):
        return str(self.id)






