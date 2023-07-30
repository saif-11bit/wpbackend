from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    service_name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200, null=True)
    sub_services = models.ManyToManyField("SubService")
    locations = models.ManyToManyField("Location")
    about = models.TextField()
    
    def __str__(self):
        return self.service_name


class Location(models.Model):
    loc = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.loc}"


class SubService(models.Model):
    sub_service_name = models.CharField(max_length=200)
    starting_price = models.IntegerField()
    
    def __str__(self):
        return f"{self.sub_service_name} - {self.starting_price}"
    

class Review(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return f"{self.service.service_name} - {self.stars}"
    
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return f"{self.user.username} - {self.user.email}"