from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.contrib.auth.models import AbstractUser


    
class UserEvent(models.Model):
    user =  models.ForeignKey(User, null = True, on_delete= models.SET_NULL, db_column='user')
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic')

    date_created =  models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Events(models.Model):
    STATUS = [
         ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
              ]

    CLUB_CHOICES = [
        ('Spectrum', 'Spectrum'),
        ('La Fiesta', 'La Fiesta'),
        ('Coffee', 'Coffee'),
        ('Arista', 'Arista'),
        ('Xpressions', 'Xpressions'),
        ('Prakrthi', 'Prakrthi'),
        
        # Add more clubs as needed
    ]

    
    name = models.CharField(max_length=200, null=True)
    club = models.CharField(max_length=200, null=True, choices=CLUB_CHOICES)   
    category = models.CharField(max_length=200, null=True, choices=STATUS)
    time = models.TimeField(null=True)
    venue = models.CharField(max_length=200, null=True)
    team_size = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_event = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_free = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def __str__(self):
        return self.name

class regEvents(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    User = models.ForeignKey(User, null = True, on_delete= models.SET_NULL)
    Events =  models.ForeignKey(Events, null = True, on_delete= models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=200, null=True)
    
class Feedback(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Feedback for {self.event.name} by {self.user.username}"


class partcipateEvents(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, db_column='user')
    phone = models.CharField(max_length=200, null=True, db_column='phone')
    email = models.CharField(max_length=200, null=True, db_column='email')
    team_size =models.IntegerField()
    part_event_id = models.AutoField(primary_key=True)
    event_name = models.ForeignKey(Events, on_delete=models.SET_NULL, null=True, db_column='name')

    def __str__(self):
        return f"Participant: {self.user} - Event: {self.event_name}"