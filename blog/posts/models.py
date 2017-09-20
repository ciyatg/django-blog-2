from django.db import models

#Each class is a table, each variable is a column in the database.

class Post(models.Model): #Post inherits from models.Model
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
