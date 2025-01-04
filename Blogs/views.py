from django.shortcuts import render
from . models import BlogModel
# Create your views here.
def blog(request, id):
    blog = BlogModel.objects.get(id = id)
    return render(request, "blogDetails.html", {"blog":blog,})