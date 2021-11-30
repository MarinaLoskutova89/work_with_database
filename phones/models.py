from autoslug import AutoSlugField
from django.db import models


class Phone(models.Model):
    name = models.TextField()
    image = models.ImageField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.TextField()
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='name')

    def __str__(self):
        return self.name
