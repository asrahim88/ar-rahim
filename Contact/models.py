from django.db import models


# Create your models here.
from django.db import models
class SocialInformation(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    github = models.URLField(max_length=300, blank=True, null=True, help_text="Your GitHub profile link")
    twitter = models.URLField(max_length=300, blank=True, null=True, help_text="Your Twitter profile link")
    linkedin = models.URLField(max_length=300, blank=True, null=True, help_text="Your LinkedIn profile link")
    behance = models.URLField(max_length=300, blank=True, null=True, help_text="Your behance profile link")
    dribble = models.URLField(max_length=300, blank=True, null=True, help_text="Your dribble profile link")
    instagram = models.URLField(max_length=300, blank=True, null=True, help_text="Your instagram profile link")
    facebook = models.URLField(max_length=300, blank=True, null=True, help_text="Your facebook profile link")
    reddit = models.URLField(max_length=300, blank=True, null=True, help_text="Your reddit profile link")
    whatsApNumber = models.CharField(max_length=25, blank=True, null=True, help_text="Your whatsApp number")
    skype = models.CharField(max_length=25, blank=True, null=True, help_text="Your Skype")
    phone_number = models.CharField(max_length=25, blank=True, null=True, help_text="Your phone number ")
    email1 = models.EmailField(max_length=100, blank=True, null=True, help_text="Your email address 2")
    email2 = models.EmailField(max_length=100, blank=True, null=True, help_text="Your email address 2")
    address = models.TextField(blank=True, null=True, help_text="Your address")

  
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name