from django.db import models


class Books(models.Model):

    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.IntegerField()
    pages = models.IntegerField()
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.title


