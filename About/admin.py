from django.contrib import admin
from . models import AboutModel, ExpertiseModel, ComfortableModel, FamiliarModel,HostingModel, OthersModel
from .models import Title


# Register your models here.

class AboutModelAdmin(admin.ModelAdmin):
    list_display = ["name", 'title', 'description', "background_img", "profile_img", "cv"]

class SkillsBaseAdmin(admin.ModelAdmin):
    list_display = ["skillName", "skillLogo"]
    
 
admin.site.register(AboutModel, AboutModelAdmin)
admin.site.register(ExpertiseModel, SkillsBaseAdmin) 
admin.site.register(ComfortableModel, SkillsBaseAdmin) 
admin.site.register(FamiliarModel, SkillsBaseAdmin) 
admin.site.register(HostingModel, SkillsBaseAdmin) 
admin.site.register(OthersModel, SkillsBaseAdmin) 

@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)