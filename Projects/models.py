from django.db import models


# Create your models here.

    
class AllProjects(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to="projects/photos")
    fullImage = models.ImageField(upload_to="projects/photos", blank=True, null=True)
    gitHubLink = models.URLField(max_length=500, blank=True, null=True)
    liveLink = models.URLField(max_length=500, blank=True, null=True)
    technology = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class WholeDescribe(models.Model):
    describe = models.TextField(1500, null=True, blank=True)
    
    
    def __str__(self):
        return self.describe