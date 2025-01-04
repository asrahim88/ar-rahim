from django.contrib import admin
from . models import AllProjects, WholeDescribe
# Register your models here.

class ResumeDescriptionAdmin(admin.ModelAdmin):
    list_display = ["description"]
    
class AllProjectsAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "description", "image","fullImage","gitHubLink", "liveLink", "technology"]

class WholeDescribeAdmin(admin.ModelAdmin):
    list_display=["describe"]
    

admin.site.register(AllProjects, AllProjectsAdmin)
admin.site.register( WholeDescribe, WholeDescribeAdmin)