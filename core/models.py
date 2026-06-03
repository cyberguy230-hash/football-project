from django.db import models

# Create your models here.
class Football(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Team = models.CharField(max_length=10)
    Player = models.CharField(max_length=20)

    def __str__(self):
        return self.Name