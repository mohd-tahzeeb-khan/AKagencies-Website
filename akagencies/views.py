from django.http import HttpResponse
from django.shortcuts import render, redirect
from contact.models import contactus
from contact.forms import formcontactus
from homepage.models import homepage


def index(request):
    contact=formcontactus(request.POST)
    data={'form':contact}
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


