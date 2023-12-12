from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
     
class UserProfile(models.Model):
    userID=models.OneToOneField(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=121)
    department = models.CharField(max_length=120, default='')
    role = models.CharField(max_length=120, default='')
    current_project =  models.CharField(max_length=120, default='')

    def __str__(self):
        return self.userID.username 
 
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(userID=kwargs['instance'])

post_save.connect(create_profile, sender=User)
