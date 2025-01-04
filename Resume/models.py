from django.db import models

# Create your models here.
class ResumeWholeDescription(models.Model):
    description = models.TextField(max_length=10000, blank=True, null=True)
    
    def __str__(self):
        return self.description
    
class Experience(models.Model):
    title = models.CharField(
        max_length=300, 
        blank=True, 
        null=True, 
        verbose_name="Job Title", 
        help_text="The title of the job position (e.g., Software Engineer)."
    )
    expDescription = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
        verbose_name="Whole Experience Summery",
        help_text="A brief description of whole experience."
    )
    company = models.CharField(
        max_length=300, 
        blank=True, 
        null=True, 
        verbose_name="Company Name", 
        help_text="The name of the company where you worked."
    )
    summary = models.TextField(
        max_length=1000, 
        blank=True, 
        null=True, 
        verbose_name="Experience Summary", 
        help_text="A brief description of your role and responsibilities."
    )
    start_date = models.DateField(
        verbose_name="Start Date", 
        help_text="The date when you started this job."
    )
    end_date = models.DateField(
        blank=True, 
        null=True, 
        verbose_name="End Date", 
        help_text="The date when you left this job. Leave blank if currently working."
    )
    is_current = models.BooleanField(
        default=False, 
        verbose_name="Currently Working", 
        help_text="Check if you are currently working in this position."
    )

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        ordering = ["-start_date"]  # Recent experiences will come first.

 

class Education(models.Model):
    
    university_name = models.CharField(
        max_length=300, 
        blank=True, 
        null=True, 
        verbose_name="University Name", 
        help_text="The name of your university (e.g., Harvard University)."
    )
    description = models.TextField(
        max_length=1000, 
        blank=True, 
        null=True, 
        verbose_name="Experience Summary", 
        help_text="A brief description of your role and responsibilities."
    )
    degree = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name="Education Degree", 
        help_text="The degree of your education (e.g., Bsc, Msc)."
    )
    
    start_date = models.DateField(
        verbose_name="Start Date", 
        help_text="The date when you started this job."
    )
    
    end_date = models.DateField(
        blank=True, 
        null=True, 
        verbose_name="End Date", 
        help_text="The date when you left this job. Leave blank if currently working."
    )
    
    is_current = models.BooleanField(
        default=False, 
        verbose_name="Currently Working", 
        help_text="Check if you are currently working in this position."
    )
    
    class Meta:
        ordering = ["-start_date"]
    
    def __str__(self):
        return self.university_name