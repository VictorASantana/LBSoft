from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Chair(models.Model): 
    id_chair = models.PositiveIntegerField(unique=True)
    is_occupied = models.BooleanField(default=False)

    class Meta: 
        db_table = "chair"


