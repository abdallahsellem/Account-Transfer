import uuid
from django.db import models

# Create your models here.

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner_name=models.CharField(max_length=256, null=False, blank=False)
    balance=models.DecimalField(max_digits=10,decimal_places=2)
    
    