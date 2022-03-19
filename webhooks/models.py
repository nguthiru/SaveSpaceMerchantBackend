from django.db import models
from products.models import Product
from authentication.models import Account
# Create your models here.
from django.utils import timezone

class OrganisationalWebhook(models.Model):
    organisation = models.OneToOneField(Account,on_delete=models.CASCADE)
    webhookUrl = models.URLField()
       


class WebHookLog(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    data = models.JSONField()
    date_created = models.DateTimeField(default=timezone.now)

