from django.db import models

# Create your models here.
class Area(models.Model):
	area_type = models.TextField(default='')

class Item(models.Model):
	text = models.TextField(default='')
	item_type = models.TextField(default='')
	area = models.ForeignKey(Area, default=None, on_delete=models.CASCADE)