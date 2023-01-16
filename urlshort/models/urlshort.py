from django.db import models
from django.shortcuts import redirect

class Urlshortadd(models.Model):
    original_url = models.CharField(max_length=500)
    shortend_url = models.CharField(max_length=500)
    keyword      = models.CharField(max_length=10)

    def addtheurl(self):
        self.save()

