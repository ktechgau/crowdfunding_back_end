from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum



class Project(models.Model):

   CATEGORY_CHOICES=[
      ("AGRI", 'Agriculture'),
      ("ARCHITECTURE", 'Architecture, Construction & Planning'),
      ("BUSINESS", 'Business Management & Entrepreneurship'),
      ("CREATIVE", 'Creative arts & Design'),
      ("EDUCATION", 'Teaching, Education & Training'),
      ("ENGINEERING", 'Engineering, Automation & Technology'),
      ("ENVIRONMENTAL", 'Environmental Science & Sustainability'),
      ("HEALTH", 'Health, Medicine, Psychology'),
      ("IT", 'IT and Computing'),
      ("LAW", 'Law, Paralegal'),
      ("MEDIA", 'Media & Communications'),
      ("PERSONAL", 'Personal Care, Beauty & Hair, Fitness'),
      ("SCIENCES", 'Sciences and Mathematics'),
      ("SOCIETY", 'Society, Culture & Humanities'),
      ("TRAVEL", 'Travel, Tourism & Hospitality'),
      ("VET", 'Veterinary Medicine'),
      ("OTHER", 'Other'),
   ]

   title = models.CharField(max_length=200)
   description = models.TextField()
   goal = models.IntegerField()
   image = models.URLField()
   is_open = models.BooleanField()
   date_created = models.DateTimeField()
   category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default="AGRI")
   owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='owned_projects'
   
 )
   

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

