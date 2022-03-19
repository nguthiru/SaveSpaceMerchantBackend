from django.db import models
from authentication.models import Account
# Create your models here.
class Product(models.Model):
    organisation = models.ForeignKey(Account,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    productUrl = models.URLField(blank=True,null=True)
    imageUrl = models.URLField()
    organisationProductID = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=100,decimal_places=2)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name

# class UserSaving(models.Model):
#     name = models.CharField(max_length=255)
#     currentAmount = models.DecimalField(max_digits=100,decimal_places=2)

class ProductSavings(models.Model):
    space = models.CharField(max_length=100,unique=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    userDetails = models.JSONField()
    currentAmount = models.DecimalField(max_digits=100,decimal_places=2)

    def __str__(self) -> str:
        return self.product





