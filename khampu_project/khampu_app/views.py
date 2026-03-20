from django.shortcuts import render
from .models import SiteContent, Temple, Festival, SocialLink, Activity

# Create your views here.
def homepage(request):
    # Get all dynamic content
    site_content = {}
    for content in SiteContent.objects.all():
        site_content[content.key] = content.value
    
    # Get structured data
    temples = Temple.objects.all()
    festivals = Festival.objects.all().order_by('english_date')
    social_links = SocialLink.objects.all()
    activities = Activity.objects.all()
    
    context = {
        'site_content': site_content,
        'temples': temples,
        'festivals': festivals,
        'social_links': social_links,
        'activities': activities,
    }
    return render(request, "index.html", context)