from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class TextEquation(models.Model):
	head = models.CharField(max_length=250)
	equation = models.CharField(max_length=250)

	def __str__(self):
		return str(self.equation)


class Image(models.Model):
    """ Image of person """
    file = models.ImageField(upload_to='photos/%Y/%m/%d', null=True,
                             blank=True)
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file.url