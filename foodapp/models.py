from django.db import models
class Food(models.Model):
    vitaminpresent=models.CharField(max_length=200)
    type2=models.CharField(max_length=150)
    name1=models.CharField(max_length=200)
