from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your user models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.TextField( max_length = 200, blank=True,null=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profiles/',default='profiles/user-default.png')
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    
    def __str__(self):
        return str(self.user.username)
    
    

