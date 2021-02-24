from django.db import models

# Create your models here.
# from django.db import models

class Menu(models.Model):
    LIGHTS = 'Lights'
    FILLERS = 'Fillers'
    DRINKS = 'Drinks'

    CATEGORIES = [
        (LIGHTS, 'Lights'),
        (FILLERS, 'Fillers'),
        (DRINKS, 'drinks'),
    ]

    text = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    count = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    def __str__(self):
        return self.text[:50]

class Order(models.Model):
    name = models.CharField(max_length=255)
    order_items = models.JSONField(encoder=None, decoder=None, null=True)
