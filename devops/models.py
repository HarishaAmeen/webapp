from django.db import models

# Create your models here.
class Cloud(models.Model):
	provider = models.CharField(max_length=250)
	rank = models.CharField(max_length=3)
	provider_logo = models.CharField(max_length=1000)

class Service(models.Model):
	cloud = models.ForeignKey(Cloud, on_delete = models.CASCADE)
	service_type = models.CharField(max_length=50)
	service_charges = models.CharField(max_length=50)


