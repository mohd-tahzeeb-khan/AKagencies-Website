from django.http import HttpResponse
from django.shortcuts import render, redirect
from contact.models import contactus, contact_details
from contact.forms import formcontactus
from service.models import services
from homepage.models import homepage, navbar
from testimonials.models import testimonials
from projects.models import project
from team.models import team
from partner.models import partners

def index(request):
    contact=formcontactus(request.POST)
    servies=services.objects.all
    home=homepage.objects.all
    nav=navbar.objects.all
    testimonial=testimonials.objects.all
    projects=project.objects.all
    teams=team.objects.all
    contacts=contact_details.objects.all
    brands=partners.objects.all
    data={'form':contact,
    'homepage':home,
    'service':servies,
    'testimonial':testimonial,
    'project':projects,
    'team':teams,
    'contact_detail':contacts,
    'brand':brands,
    'navbar':nav
    }

    return render(request, "index.html", data)
def savecontact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobileno=request.POST.get('mobileno')
        description=request.POST.get('description')
        savedata=contactus(name=name, email=email, mobile=mobileno, message=description)
        savedata.save()
        return redirect(index)


