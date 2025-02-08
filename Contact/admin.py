from django.contrib import admin
from . models import SocialInformation,ContactMessage

# Register your models here.

class SocialInformationAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "github", "twitter", "linkedin","behance","reddit","dribble","facebook","instagram", "whatsApNumber","skype","phone_number", "email1","email2", "address"]
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject","message", "created_at"]
    
admin.site.register(SocialInformation, SocialInformationAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)