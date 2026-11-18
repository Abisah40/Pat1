from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
#naming convention is important when it comes to 
class User(AbstractUser):
    #status = models.CharField(max_length=225, choices=[('status','active'),('status','inactive')])
    # first_name = models.CharField(max_length=55)
    # last_name = models.CharField(max_length=55)
    # email = models.EmailField(unique=True)
    is_active=True
    bio = models.TextField(blank=True,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone = models.CharField(max_length=15,blank=True,null=True)
    facebook = models.URLField(max_length=50,blank=True,null=True)
    whatsapp = models.URLField(max_length=50,blank=True,null=True)
    images = models.ImageField(upload_to='profile_picture',blank=True,null=True)
    # last_login = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.username