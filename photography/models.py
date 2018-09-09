from django.db import models

class Photography(models.Model):
	image = models.ImageField(upload_to="photos/")
