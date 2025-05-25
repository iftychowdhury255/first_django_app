from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50),
    email = models.EmailField()
    age = models.IntegerField()
    isMaried = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name