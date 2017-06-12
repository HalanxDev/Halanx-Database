from django.db import models


class User(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # UserName = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    PhoneNo = models.BigIntegerField(unique=True, null=True)
<<<<<<< HEAD
    EmailId = models.EmailField(blank=True)
    FirstName = models.CharField(max_length=200, blank=True)
    LastName = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=1000, null=True)
    Address = models.CharField(blank=True, null=True, max_length=300)
    logged_in = models.BooleanField(blank=True, default=True)
=======
    PhoneNo = models.BigIntegerField(unique=True)
    EmailId = models.EmailField(blank=True)
    FirstName = models.CharField(max_length=200, blank=True)
    LastName = models.CharField(max_length=200, blank=True)
    Address = models.CharField(blank=True, null=True, max_length=300)
>>>>>>> 00fb1996c369d73bf36067bf3cd8aca96e95305e
    AvgRating = models.FloatField(default=3.0, blank=True)
    n = models.IntegerField(default=0, blank=True)     # denotes number of times user has been rated

    def __str__(self):
<<<<<<< HEAD
        return str(self.PhoneNo)
=======
        return str(self.id)
>>>>>>> 00fb1996c369d73bf36067bf3cd8aca96e95305e






