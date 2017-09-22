from django.db import models
from django.utils import timezone

#Each class is a table, each variable is a column in the database.

class WasHere(models.Model): #Post inherits from models.Model. With this way Django knows that WasHere is a model and should be saved in the database.
    name = models.CharField(max_length = 40)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #This is the publish method.
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.name
