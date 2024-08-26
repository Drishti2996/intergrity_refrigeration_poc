from django.db import models
import uuid

class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default="No name available")
    description = models.TextField(default="No description available")
    fridge_id = models.CharField(max_length=50, default="No fridge ID")
    model_number = models.CharField(max_length=50, default="No model number")
    serial_number = models.CharField(max_length=50, default="No serial number")
    purchase_date = models.DateField(null=True, blank=True)
    installation_date = models.DateField(null=True, blank=True)
    warranty_expiry_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True, default="No location")
    







