from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key = True , unique = True , null = False)
    name = models.ForeignKey(User , on_delete = models.CASCADE)
    rank = models.CharField(max_length = 10)
    password = models.CharField(max_length = 10)
    def __str__(self):
        return self.name


class Images(models.Model):
    added_by = models.ForeignKey(UserProfile , on_delete = models.CASCADE)
    img_name = models.CharField()
    images_file = models.ImageField(upload_to="static")

# Website Content Models
class SiteContent(models.Model):
    """Manage dynamic content for the website"""
    key = models.CharField(max_length=100, unique=True, help_text="Unique identifier for the content")
    value = models.TextField(help_text="Content value")
    content_type = models.CharField(max_length=20, choices=[
        ('text', 'Text'),
        ('html', 'HTML'),
        ('image', 'Image'),
        ('link', 'Link'),
    ], default='text')
    
    def __str__(self):
        return f"{self.key}: {self.value[:50]}..."

class Temple(models.Model):
    """Manage temple information"""
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="temples/")
    caption = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class Festival(models.Model):
    """Manage festival events"""
    name = models.CharField(max_length=100)
    english_date = models.DateField()
    nepali_date = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class SocialLink(models.Model):
    """Manage social media links"""
    title = models.CharField(max_length=100)
    url = models.URLField()
    icon_class = models.CharField(max_length=50, help_text="Font Awesome icon class")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class Activity(models.Model):
    """Manage activity sections"""
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to="activities/")
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title
    