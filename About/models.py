from django.db import models

# Create your models here.
class AboutModel(models.Model):
    name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=400, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    background_img = models.ImageField(upload_to="background/photos", blank=True, null=True)
    profile_img = models.ImageField(upload_to="profile/photos", blank=True, null=True)
    cv = models.FileField(upload_to="cv/uploads", blank=True, null=True)  # PDF আপলোডের জন্য ফাইল ফিল্ড
    
    def __str__(self):
        return self.name

class SkillBaseModel(models.Model):
    skillName = models.CharField(max_length=100, null=True, blank=True)
    skillLogo = models.ImageField(upload_to="logo/photos", null=True, blank=True)

    def __str__(self):
        return self.skillName

    class Meta:
        abstract = True  


class ExpertiseModel(SkillBaseModel):
    pass
class ComfortableModel(SkillBaseModel):
    pass
class FamiliarModel(SkillBaseModel):
    pass
class HostingModel(SkillBaseModel):
    pass
class OthersModel(SkillBaseModel):
    pass