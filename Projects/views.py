from django.shortcuts import render
from .models import AllProjects, WholeDescribe

# Create your views here.
def showProjects(request):
    projects = AllProjects.objects.all()
    projectIntro = WholeDescribe.objects.all()
    context = {
        "allProjects": projects,
        "projectIntro": projectIntro[0]
        }
    return render(request, "allProjects.html", context)