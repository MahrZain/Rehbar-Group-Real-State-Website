from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=60, null=True)
    description = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=60, null=True)
    description = models.TextField(max_length=100, null=True)
    image = models.ImageField(upload_to='about_images/', null=True,help_text="height: 1178 px width: 1775 px")
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=60, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    working_hours = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.address
    
class SocialMedia(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
    ]
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.platform
    
class Service(models.Model):    
    icon_class = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=60, null=True)
    description = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.title
    
class client(models.Model):
    number = models.CharField(max_length=15, null=True)
    name = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.name
    
class Feature(models.Model):
    title = models.CharField(max_length=60, null=True)
    description = models.TextField(max_length=100, null=True)
    image = models.ImageField(upload_to='feature_images/', null=True, help_text="height: 1178 px width: 1775 px")

    def __str__(self):
        return self.title