from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum

# Create your models here.

class Project(models.Model):
 title = models.CharField(max_length=200)
 description = models.TextField()
 goal = models.IntegerField()
 image = models.URLField()
 is_open = models.BooleanField()
 date_created = models.DateTimeField()
 owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='owned_projects'
 )

# Getting sum of pledge for that project
#@property
#def pledge_total(self):
   #return self.pledges.aggregate(
      #total=Sum('amount'))['total']

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
       get_user_model(),
       on_delete=models.CASCADE,
       related_name='supported_pledges'
    )
