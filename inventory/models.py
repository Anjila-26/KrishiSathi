from django.db import models
    
class Stock(models.Model):
    ANIMAL = 'animal'
    PLANT = 'plant'
    DEFAULT_TYPE = PLANT  # or PLANT, depending on your preference
    
    TYPE_CHOICES = [
        (ANIMAL, 'Animal'),
        (PLANT, 'Plant'),
    ]
    
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, default=DEFAULT_TYPE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)
    breed = models.CharField(max_length=30, unique=False, default= 'british')

    def __str__(self):
	    return self.name