from django.db import models

from users.models import User
 
class Site(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url=models.CharField(max_length=100)
