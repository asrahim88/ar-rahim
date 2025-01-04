from django.contrib import admin
from . models import BlogModel, WholeBlogDescribe
        
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "description"]
    
class WholeBlogDescribeAdmin(admin.ModelAdmin):
    list_display = ["wholeTitle", "description"]
    
admin.site.register(BlogModel, BlogModelAdmin)
admin.site.register(WholeBlogDescribe, WholeBlogDescribeAdmin)