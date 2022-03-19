from curses import def_prog_mode
from django.db import models

# Create your models here.
class Account(models.Model):
    organisation = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    website = models.URLField(null=True,blank=True)
    active = models.BooleanField(default=False)
    organisationNumber = models.CharField(max_length=20)



    def __str__(self) -> str:
        return self.organisation




    
