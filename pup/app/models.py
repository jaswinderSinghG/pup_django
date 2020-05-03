from django.db import models
#import datetime
#from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class social_notice_data(models.Model):
    public_notice = models.TextField(max_length = 500, blank = False)
    pub_date = models.DateTimeField(auto_now_add = True)


class user_form(models.Model):
    Name = models.CharField(max_length = 500, blank = False)
    Father_Name = models.CharField(max_length = 500, blank = False)
    Village = models.CharField(max_length = 500, blank = False)
    Mobile_Number = models.IntegerField(blank=True)
    Message = models.CharField(max_length = 150, blank = False)


class running_activities(models.Model):
    Title = models.CharField(max_length=100, blank = False)
    explanation = models.TextField(max_length = 100, blank = False)
    image=models.FileField(blank = False)
    pub_date = models.DateTimeField(auto_now_add = True)



###############################################Nainewal#######
class Sarpanch_Name_Pic(models.Model): #Here is Sarpanch mean members model
    full_name = models.CharField(max_length=70, null = True)
    Mobile_Number = models.IntegerField(blank=True, null=True)
    image=models.FileField(blank = False, null = True) #max_length=100


class Home_Page_Pics_Article(models.Model):
    home_fixed_image = models.FileField(upload_to = 'homeImagesFixed') 
    best_article = models.TextField(max_length=2000, blank = True)


class Home_Dynamic_Pics(models.Model):
    home_dynamic_images = models.FileField(upload_to = 'dynamicPics_folder/')


class Admin_Name_Pic(models.Model):
    base_admin_pic = models.FileField(blank = False, upload_to = 'AdminPics/')
    base_admin_name = models.CharField(max_length = 100)
        

class School_Data(models.Model):
    image_of_year = models.FileField(blank = False, upload_to = 'School/')
    name_of_student = models.CharField(max_length = 100, blank = False)
    quote = models.CharField(max_length = 100)


class School_admission(models.Model):
    mentor_name = models.CharField(max_length = 100, blank = False)
    mobile_Number = models.IntegerField(blank=False, null=True)

    notice = models.CharField(max_length = 100, blank = False)
