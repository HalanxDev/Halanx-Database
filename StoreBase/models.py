from django.db import models
from Products.models import Product


class Store(models.Model):

    # NAME, ADDRESS OF STORE
    StoreName = models.CharField(blank=True, null=True, max_length=200)
    StoreAddress = models.CharField(max_length=300, null=True, blank=True)

    # DEALER DETAILS
    Dealer_FirstName = models.CharField(max_length=200, null=True, blank=True)
    Dealer_LastName = models.CharField(max_length=200, null=True, blank=True)
    Dealer_ContactNo = models.BigIntegerField(null=True, blank=True)
    Dealer_EmailId = models.EmailField(blank=True, null=True)
    Dealer_password = models.CharField(max_length=1000, blank=True, null=True)
    Dealer_Designation = models.CharField(max_length=100, blank=True, null=True)

    # LOCATION DETAILS
    Latitude = models.FloatField(blank=True, null=True)
    Longitude = models.FloatField(blank=True, null=True)

    # BUSINESS DETAILS
    CompanyLegalName = models.CharField(max_length=300, blank=True, null=True)
    PANNumber = models.CharField(max_length=50, blank=True, null=True)
    # Logo images ??

    # BANK ACCOUNTS DETAILS
    BankAccountNumber = models.CharField(max_length=50, blank=True, null=True)
    BankAccountType = models.CharField(max_length=10, blank=True, null=True)
    BankName = models.CharField(max_length=200, blank=True, null=True)
    BankBranch = models.CharField(max_length=300, blank=True, null=True)
    BankBranchAddress = models.CharField(max_length=300, blank=True, null=True)
    IFSCCode = models.CharField(max_length=25, blank=True, null=True)

    # PRODUCTS AVAILABLE
    ProductsAvailable = models.ManyToManyField(Product, blank=True)

    Active = models.BooleanField(blank=True, default=True)              # don't know if this is required or not
                                                            # as if store is deleted all its products will be too

    # AVAILABILITY DETAILS
    OpeningTime = models.TimeField(null=True, blank=True)
    ClosingTime = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.StoreName





