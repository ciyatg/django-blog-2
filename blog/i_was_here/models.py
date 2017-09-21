from django.db import models

#Each class is a table, each variable is a column in the database.

class was_here(models.Model): #Post inherits from models.Model
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name
