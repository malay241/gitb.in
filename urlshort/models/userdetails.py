from django.db import models

class UserDetails(models.Model):
    date = models.CharField(max_length=10)
    hostname = models.CharField(max_length=50)
    userip = models.CharField(max_length=20)
    country = models.CharField(max_length=15)
    region = models.CharField(max_length=20)
    city = models.CharField(max_length=50)

    def adduserdetails(self):
        self.save()




      