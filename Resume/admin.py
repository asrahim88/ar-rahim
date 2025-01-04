from django.contrib import admin
from . models import Experience, Education, ResumeWholeDescription

# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["expDescription","company", "title","start_date", "end_date", "is_current", "summary",]
    
class EducationAdmin(admin.ModelAdmin):
    list_display = ["university_name", "description", "degree", "start_date", "end_date", "is_current"]

class ResumeWholeDescriptionAdmin(admin.ModelAdmin):
    list_display = ["description"]
    
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(ResumeWholeDescription, ResumeWholeDescriptionAdmin)