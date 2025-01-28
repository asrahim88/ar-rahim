from django.shortcuts import render, redirect
from About.models import AboutModel, ExpertiseModel, ComfortableModel, FamiliarModel, HostingModel, OthersModel, Title
from Resume.models import Experience, Education, ResumeWholeDescription
from Blogs.models import BlogModel, WholeBlogDescribe
from Projects.models import  AllProjects, WholeDescribe
from Contact.models import SocialInformation
from Contact.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse


def home(request):
    info = AboutModel.objects.all()
    expertise = ExpertiseModel.objects.all()
    comfortable = ComfortableModel.objects.all()
    familiar = FamiliarModel.objects.all()
    hosting = HostingModel.objects.all()
    others = OthersModel.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    ResumeWholeDesc = ResumeWholeDescription.objects.all()
    allProjects = AllProjects.objects.all()
    projectsIntro = WholeDescribe.objects.all()
    allBlogs = BlogModel.objects.all()
    wholeBlogDescribe = WholeBlogDescribe.objects.all()
    
    socialInfo = SocialInformation.objects.all()
    titles = Title.objects.all().values_list('name', flat=True)  # টাইটেল এর লিস্ট
    context = {
        "about": info[0], 
        "expSkills":  expertise, 
        "comSkills":  comfortable, 
        "famSkills":  familiar, 
        "hostSkills":  hosting, 
        "othSkills":  others, 
        "experience": experiences, 
        "educations": educations, 
        "ResumeWholeDesc": ResumeWholeDesc[0],
        "allProjects": allProjects[:4],
        "projectsIntro": projectsIntro[0],
        "allBlogs": allBlogs,
        "wholeBlogDescribe": wholeBlogDescribe[0],
        "socialInfo": socialInfo[0],
        'titles': list(titles),
        }
    
    # AJAX রিকোয়েস্ট চেক করা
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['subject'] or "New Contact Message"
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\n\nMessage:\n{form.cleaned_data['message']}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['akrahim88@gmail.com'])
            return JsonResponse({'success': True, 'message': 'Your message has been sent successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
    form = ContactForm()
    context["form"] = form
    
    return render(request, "index.html", context=context)
