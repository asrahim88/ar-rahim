from django.db import models
# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to="blog/photos", null=True, blank=True)
    description = models.TextField(max_length=10000, null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class WholeBlogDescribe(models.Model):
    wholeTitle = models.CharField(max_length=2000, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    
    def __str__(self):
        return self.description